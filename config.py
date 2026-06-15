"""
Save Restricted Content Bot Configuration

Developed by: LastPerson07Xcantarella
Telegram: @cantarellabots X @THEUPDATEDGUYS

Please retain this credit if you use or modify this project.
"""

import os


# ==============================
# Telegram Bot Credentials
# ==============================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8543161816:AAFx6xFCaC0B8gRRYmUU3G9yCCSJUPvXAEY")
API_ID = int(os.environ.get("API_ID", "35406234"))
API_HASH = os.environ.get("API_HASH", "2b617fc9589fcaa248aacfcbd8f6cf4e")


# ==============================
# Admin Configuration
# ==============================

# Add admin user IDs separated by commas in environment variables
ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "6701353840").split(",") if admin]


# ==============================
# Database Configuration
# ==============================

DB_URI = os.environ.get("DB_URI", "mongodb+srv://zerocourse2026_db_user:fmVgnjbZGfWP9BIf@cluster.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted2")


# ==============================
# Logging Configuration
# ==============================

# Replace with your Telegram log channel ID (example: -1001234567890)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003948612336"))


# ==============================
# Error Handling
# ==============================

# Set to True to send error messages to users
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
