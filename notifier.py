import requests
from plyer import notification


def trigger_os_popup(message):
    try:
        notification.notify(
            title="SysOps Health Alert",
            message=message,
            app_name="Health Daemon",
            timeout=5
        )
    except Exception as error:
        print(f"[POPUP ERROR] {error}")


def send_ntfy_alert(message):
    url = "https://ntfy.sh/nirmals_health_monitor_x932"
    try:
        response = requests.post(
            url, data=message.encode(encoding='utf-8'), timeout=5)
        print(
            f"[NETWORK DEBUG] Status: {response.status_code} | Reply: {response.text}")
    except requests.exceptions.RequestException as error:
        print(f"[NETWORK ERROR] Alert delivery failed: {error}")


def dispatch_alerts(message):
    trigger_os_popup(message)
    send_ntfy_alert(message)
