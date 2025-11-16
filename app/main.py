import asyncio
from poller import StatusPoller

if __name__ == "__main__":
    url = "https://status.openai.com/api/v2/summary.json"
    poller = StatusPoller(url=url, interval=10)

    asyncio.run(poller.start())
