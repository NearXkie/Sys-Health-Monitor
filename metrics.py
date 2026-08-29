# Import psutil library to access system hardware metrics
import psutil

# Maximum allowable CPU, RAM, Disk utilization percentage
CPU_THRESHOLD = 70
RAM_THRESHOLD = 70
DISK_THRESHOLD = 85


# Function to collect current system resource usage
def get_system_metrics():
    """Retrieves current CPU, memory usage, and disk space."""
    # Return dictionary with current CPU, RAM, and Disk utilization percentages
    return {
        # Measure CPU utilization over a 1-second window
        'CPU': psutil.cpu_percent(interval=1),
        'RAM': psutil.virtual_memory().percent,  # Get current RAM usage percentage
        # Get root drive disk usage percentage
        'Disk': psutil.disk_usage('/').percent
    }


# Function to verify if any metrics exceed defined limits
def check_thresholds(metrics):
    """Compare live data against limits and return a flag"""
    alerts = []  # Initialize empty list to store active alert messages

    # Check if CPU usage exceeds the defined threshold
    if metrics['CPU'] > CPU_THRESHOLD:
        # Record CPU breach alert
        alerts.append(f"CPU ALERT: {metrics['CPU']}%")

    # Check if RAM usage exceeds the defined threshold
    if metrics['RAM'] > RAM_THRESHOLD:
        # Record RAM breach alert
        alerts.append(f"RAM ALERT: {metrics['RAM']}%")

    # Check if Disk usage exceeds the defined threshold
    if metrics['Disk'] > DISK_THRESHOLD:
        # Record Disk breach alert
        alerts.append(f"DISK ALERT: {metrics['Disk']}%")

    # Return breach status boolean (True if alerts exist) and the list of alerts
    return bool(alerts), alerts
