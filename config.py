import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
PREFIX = os.getenv("PREFIX", "!")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Colors for embeds
COLOR_PRIMARY = 0x5865F2  # Blurple
COLOR_SUCCESS = 0x57F287  # Green
COLOR_ERROR = 0xED4245    # Red
COLOR_WARNING = 0xFAA61A  # Yellow

# Ticket categories
TICKET_CATEGORIES = {
    "bug_report": "🐛 Bug Report",
    "feature_request": "✨ Feature Request",
    "appeal": "📞 Appeal Moderation",
    "support": "🆘 General Support"
}