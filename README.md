# Shayaa Client 🍟

This script runs on a Raspberry Pi (or any Linux host) and sends basic **system health data** to a remote monitoring server.  
It reports CPU usage, memory, disk usage, temperature, hostname, and both local & public IP addresses.

Useful for:
- IoT device monitoring
- Home lab fleet visibility
- Usage dashboards and uptime checks

---

### Environment Key
```
SERVER = "https://your-server-url-here"
API_KEY = "your-user-api-key"
DEVICE_ID = "your-device-id"
```

## 📦 Requirements

### Python Packages
Install dependencies:

```bash
pip install requests psutil
```

### Run Cron Job
```
# Create Jon
crontab -e

# Run Job every minute
*/1 * * * * /usr/bin/python3 /home/pi/device_ping.py >/dev/null 2>&1

# Verify
crontab -l 
```