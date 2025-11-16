from notifier import Notifier
from models import WebhookPayload

class WebhookHandler:
    """Handles incoming webhook events."""

    def __init__(self):
        self.notifier = Notifier()

    def handle(self, payload: dict):
        data = WebhookPayload(data=payload)
        attributes = data.data.get("data", {}).get("attributes", {})

        title = attributes.get("name") or attributes.get("title", "Unknown")
        message = attributes.get("body") or attributes.get("status", "No details")

        self.notifier.notify(title, message)
