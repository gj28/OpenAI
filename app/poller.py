import asyncio
import httpx
from notifier import Notifier

from models import Component, Incident, IncidentUpdate


class StatusPoller:
    """Polls OpenAI status page and prints updates."""

    def __init__(self, url: str, interval: int = 15):
        self.url = url
        self.interval = interval
        self.notifier = Notifier()
        self.etag = None

    async def fetch(self):
        """Fetch the status JSON from OpenAI."""
        headers = {}

        if self.etag:
            headers["If-None-Match"] = self.etag

        async with httpx.AsyncClient() as client:
            response = await client.get(self.url, headers=headers)

        if response.status_code == 304:
            return None

        if response.status_code == 200:
            self.etag = response.headers.get("etag")
            return response.json()

        return None

    async def process(self, data: dict):
        """Convert JSON → Models → Print updates."""

        components = data.get("components", [])
        incidents = data.get("incidents", [])

        # Always print c
        for comp in components:
            comp_obj = Component(**comp)
            msg = (
                f"Status: {comp_obj.status}"
                if comp_obj.status != "operational"
                else "All good"
            )
            self.notifier.notify(comp_obj.name, msg)

        # Print 
        for inc in incidents:
            inc_obj = Incident(
                id=inc["id"],
                name=inc["name"],
                status=inc["status"],
                incident_updates=[
                    IncidentUpdate(**u) for u in inc.get("incident_updates", [])
                ],
            )

            if inc_obj.incident_updates:
                latest = inc_obj.incident_updates[0].body
                self.notifier.notify(inc_obj.name, latest)

    async def start(self):
        print("\nPoller started... Checking every", self.interval, "seconds\n")

        while True:
            data = await self.fetch()

            if data:
                await self.process(data)
            else:
                self.notifier.notify("Status Check", "No changes detected.")

            await asyncio.sleep(self.interval)
