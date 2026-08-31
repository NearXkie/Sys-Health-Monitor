

import logging
from plyer import notification  # false alarm


def trigger_os_popup(message):
    notification.notify(
        title="SysOps Health Alert",
        message=message,
        app_name="Health Daemon",
        timeout=5
    )


def send_email_alert(message):
    # Phase 5 SMTP logic goes here
    pass


def send_sms_alert(message):
    # Phase 5 Twilio logic goes here
    pass


def dispatch_alerts(message):
    trigger_os_popup(message)
    # Phase 5: Add fallback logic here (e.g., if email fails, try SMS)
