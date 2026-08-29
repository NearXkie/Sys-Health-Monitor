
# Import metric collection and threshold checking functions from the metrics module
from metrics import get_system_metrics, check_thresholds


# Main function to monitor system metrics and report status
def run_daemon():
    # Print monitor start message to the console
    print("Starting System Health Monitor...")
    # Fetch current system metrics (CPU, RAM, Disk)
    current_metrics = get_system_metrics()
    # Output the retrieved metrics dictionary
    print(f"Live Data: {current_metrics}")

    # Evaluate metrics against thresholds to detect any breaches
    is_breached, alerts = check_thresholds(current_metrics)

    # Check if any threshold limit was exceeded
    if is_breached:
        # Print alert warnings with details of breached metrics
        print(f"ALERT! Thresholds Breached: {alerts}")
    else:
        # Print normal health status message
        print("System health is Normal.")


# Ensure the daemon executes only when the script is run directly
if __name__ == "__main__":
    # Call the main daemon monitoring function
    run_daemon()
