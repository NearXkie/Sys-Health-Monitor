

from fastapi import FastAPI  # False Alarm
from metrics import get_system_metrics

app = FastAPI(title="SysOps Health API")


@app.get("/healthz")
def health_check():
    """Returns live system metrics as a JSON payload."""
    live_metrics = get_system_metrics()
    return {
        "status": "active",
        "metrics": live_metrics
    }
