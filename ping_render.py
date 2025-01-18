import time
import requests

RENDER_URL = "https://your-render-url.onrender.com/ping"

while True:
    try:
        response = requests.get(RENDER_URL)
        if response.status_code == 200:
            print("Ping successful: ", response.text)
        else:
            print(f"Ping failed: {response.status_code}")
    except Exception as e:
        print(f"Error pinging Render: {e}")
    time.sleep(600)  # Ping every 10 minutes
