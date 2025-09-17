import os

# It's highly recommended to use environment variables for sensitive data.
# On your server, you would set these variables instead of hardcoding them here.
# Example: export TELEGRAM_TOKEN="your_real_token"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7981260485:AAF-6REyvM54C_Vh5uo1z-PxK9eD1zl8hpA")
ADMIN_ID = int(os.getenv("ADMIN_ID", 6573039473))

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

# --- Payment Numbers ---
MTN_NUMBER = "+2290167750083"