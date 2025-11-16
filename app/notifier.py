from datetime import datetime

class Notifier:
    """Responsible for printing notifications."""

    def notify(self, title: str, message: str):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

        print("\n-----------------------------------")
        print(f"[{timestamp}]")
        print(f"Service : {title}")
        print(f"Message : {message}")
        print("-----------------------------------\n")
