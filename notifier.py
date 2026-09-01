

import requests
from plyer import notification  # false alarm


def trigger_os_popup(message):
    notification.notify(
        title="SysOps Health Alert",
        message=message,
        app_name="Health Daemon",
        timeout=5
    )


def send_ntfy_alert(message):
    # Ensure this URL is exact, with no trailing slashes
    url = "https://ntfy.sh/nirmals_health_monitor_x932"

    # Capture the server's response
    response = requests.post(url, data=message.encode(encoding='utf-8'))

    # Print the exact HTTP status code and server error text
    print(
        f"[NETWORK DEBUG] Status: {response.status_code} | Reply: {response.text}")


def dispatch_alerts(message):
    trigger_os_popup(message)
    send_ntfy_alert(message)
