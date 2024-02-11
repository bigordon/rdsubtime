import requests
import json
import time

REAL_DEBRID_API_KEY = 'YOUR_REAL_DEBRID_API_KEY'
PLEX_WEBHOOK_URL = 'YOUR_PLEX_WEBHOOK_URL'
CHECK_INTERVAL = 86400  # 24 hours in seconds

def check_subscription():
    # Make a request to Real Debrid API to get subscription status
    real_debrid_url = f'https://api.real-debrid.com/rest/1.0/user?auth_token={REAL_DEBRID_API_KEY}'
    response = requests.get(real_debrid_url)
    data = response.json()
    
    # Extract subscription information
    subscription_end_date = data['subscription_end']
    
    # Calculate days until subscription ends
    today_timestamp = int(time.time())
    days_until_expiry = (subscription_end_date - today_timestamp) / (3600 * 24)
    
    return days_until_expiry

def send_notification():
    # Send notification to Plex via webhook
    payload = {
        "payload": {
            "notification": "Your Real Debrid subscription is expiring soon. Please renew!"
        }
    }
    requests.post(PLEX_WEBHOOK_URL, json=payload)

def main():
    while True:
        days_until_expiry = check_subscription()

        if days_until_expiry <= 30:
            send_notification()
            print("Notification sent to Plex!")
        else:
            print("Subscription is still valid.")

        # Wait for specified interval before checking again
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
