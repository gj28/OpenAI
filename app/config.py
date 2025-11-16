from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    """Simple configuration loader (OOP)."""

    STATUS_URL = os.getenv("STATUSPAGE_URL", "https://status.openai.com/api/v2/summary.json")
    POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 20))
    WEBHOOK_MODE = os.getenv("WEBHOOK_MODE", "false").lower() == "true"

settings = Settings()
