import logging
import time
from metrics import get_system_metrics, check_thresholds
from notifier import dispatch_alerts

logging.basicConfig(
    filename='health_daemon.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def run_daemon(poll_interval=60):
    logging.info("System Health Daemon initialized.")
    print(
        f"Daemon running. Polling every {poll_interval}s. Press Ctrl+C to stop.")

    try:
        while True:
            metrics = get_system_metrics()
            is_breached, alerts = check_thresholds(metrics)

            if is_breached:
                warning_msg = f"Threshold breached: {', '.join(alerts)}"
                print(f"[ALERT] {warning_msg}")
                logging.warning(warning_msg)
                dispatch_alerts(warning_msg)
            else:
                logging.info(f"System healthy: {metrics}")

            time.sleep(poll_interval)

    except KeyboardInterrupt:
        print("\nShutdown signal received. Stopping daemon cleanly...")
        logging.info("System Health Daemon stopped by user.")
    except Exception as error:
        logging.critical(
            f"Daemon crashed unexpectedly: {error}", exc_info=True)
        print(f"[CRITICAL] Daemon crashed: {error}")


if __name__ == "__main__":
    run_daemon(poll_interval=60)
