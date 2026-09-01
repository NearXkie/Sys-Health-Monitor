
# System Health Monitor

> Check CPU, RAM and Disk Metrics 

---
## Architectur
---

### - Core Library: psutil (Python System and Process Utilities)
### - Dictionaries to Cleanly map point-in-metrics
>  {'cpu'}: 50.1, 'ram': 70.1, 'disk': 19.7}
### - Logic Engine: Validation Function
    - Compare Live data with Thresholds 
    - Simple boolens to flag
### - Execution: while True as main block

---
## Phase
---

### - Phase 1: Environment and Metric Extraction
    - Initialize clean git repo, and virtual env
    - Install psutil in terminal
    - Write isolated transformation functions to retrieve and print current CPU percentages, memory usage, and disk space

### - Phase 2: Thresholds and Logic
    - Define warning limits as global variables 
    - Write comparision logic to trigger a true/ false flag if threshold is exceeded 
    
### - Phase 3: Logging and Orchestration
    - Use python built-in logginh module to write time-stamped warnings to health_daemon.log file
    - Wrap extraction and validation steps inside a central orchestrator function
    - Run the orchestrator inside infinite loop, using try/ except block to handle any unexpected crashes.

##### - Phase 4: System Tray Notifications
    - Set up a minimal UI with plyer for a basic notification
    - Trigger a subtle popup or system notification when a threshold is breached
    - Add an exit listener to cleanly shut down the daemon

##### - Phase 5: External Notifications (Email/SMS)
    - Used ntfy for mobile notifications
---
###  OUT OF SCOPE (Future Scope/Expansion of Scope)

##### - Phase 6: Health Check Endpoint
    - Create a small Flask or FastAPI web server to expose health_status on an HTTP endpoint
    - Add a /healthz route that returns JSON metrics for container orchestration tools (Kubernetes/Docker Swarm) to consume
