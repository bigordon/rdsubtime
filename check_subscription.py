import requests
import json
import time
from datetime import datetime

def read_config():
    with open('config.json') as f:
        return json.load(f)

def check_subscription(api_key):
    # Make a request to Real Debrid API to get subscription status
    real_debrid_url = f'https://api.real-debrid.com/rest/1.0/user?auth_token={a>
    response = requests.get(real_debrid_url)
    data = response.json()
    
    # Extract expiration information
    expiration_str = data['expiration']
    
    # Parse expiration date to a timestamp
    try:
        expiration = int(expiration_str)
    except ValueError:
        # Handle if the date is in a different format
        expiration = int(datetime.strptime(expiration_str.split('T')[0], "%Y-%m>
    
    # Calculate days until expiration
    today_timestamp = int(time.time())
    days_until_expiry = (expiration - today_timestamp) / (3600 * 24)
    
    return days_until_expiry

def send_notification(webhook_url, days_left):
    # Round to whole number
    rounded_days_left = round(days_left)

    # Send notification to Discord via webhook
    payload = {
        "content": f"Your Real Debrid subscription is expiring in {rounded_days>
    }
    requests.post(webhook_url, json=payload)

def main():
    config = read_config()
    api_key = config['real_debrid_api_key']
    webhook_url = config['discord_webhook_url']
    check_interval = config['check_interval']
    
    while True:
        days_until_expiry = check_subscription(api_key)

        if days_until_expiry <= 30: # change to how ever many days until expiration
            send_notification(webhook_url, days_until_expiry)
            print("Notification sent to Discord!")
        else:
            print("Subscription is still valid.")

        # Wait for specified interval before checking again
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
    
