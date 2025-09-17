import os

# It's highly recommended to use environment variables for sensitive data.
# On your server, you would set these variables instead of hardcoding them here.

# Load sensitive data from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID_STR = os.getenv("ADMIN_ID")
MTN_NUMBER = os.getenv("MTN_NUMBER")

# Validate that the essential variables are set
if not TELEGRAM_TOKEN:
    raise ValueError("No TELEGRAM_TOKEN set for bot. Please set it in your environment variables.")
if not ADMIN_ID_STR:
    raise ValueError("No ADMIN_ID set for bot. Please set it in your environment variables.")

try:
    ADMIN_ID = int(ADMIN_ID_STR)
except ValueError:
    raise ValueError("ADMIN_ID must be an integer.")

# --- Price Configuration ---
# Centralized price map to ensure consistency across the application
PRICE_MAP = {
    'montante': 3000, 
    'vip': 5000,
    'trial': 0  # Trial is free
}

# --- Affiliate Links ---
LINK_1XBET = "https://1xlite-437776.top/mobile?bf=254b48663f5c4_5342613771"
LINK_MELBET = "https://melbet.org/mobile?bf=12e097f0b9354_5536012235"
