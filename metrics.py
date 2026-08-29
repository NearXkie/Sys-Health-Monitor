# Import psutil library to access system hardware metrics
import psutil

# Maximum allowable CPU utilization percentage
CPU_THRESHOLD = 70
# Maximum allowable RAM utilization percentage
RAM_THRESHOLD = 70
# Maximum allowable Disk utilization percentage
DISK_THRESHOLD = 85


# Function to collect current system resource usage
def get_system_metrics():
    """Retrieves current CPU, memory usage, and disk space."""
    # Return dictionary with current CPU, RAM, and Disk utilization percentages
    return {
        'CPU': psutil.cpu_percent(interval=1),  # Measure CPU utilization over a 1-second window
        'RAM': psutil.virtual_memory().percent,  # Get current RAM usage percentage
        'Disk': psutil.disk_usage('/').percent   # Get root drive disk usage percentage
    }


# Function to verify if any metrics exceed defined limits
def check_thresholds(metrics):
    """Compare live data against limits and return a flag"""
    alerts = []  # Initialize empty list to store active alert messages

    # Check if CPU usage exceeds the defined threshold
    if metrics['CPU'] > CPU_THRESHOLD:
        alerts.append(f"CPU ALERT: {metrics['CPU']}%")  # Record CPU breach alert

    # Check if RAM usage exceeds the defined threshold
    if metrics['RAM'] > RAM_THRESHOLD:
        alerts.append(f"RAM ALERT: {metrics['RAM']}%")  # Record RAM breach alert

    # Check if Disk usage exceeds the defined threshold
    if metrics['Disk'] > DISK_THRESHOLD:
        alerts.append(f"DISK ALERT: {metrics['Disk']}%")  # Record Disk breach alert

    # Return breach status boolean (True if alerts exist) and the list of alerts
    return bool(alerts), alerts

