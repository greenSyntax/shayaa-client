import requests
import socket
from datetime import datetime
import psutil
import subprocess

# Production Server
SERVER = "https://sea-lion-app-xt845.ondigitalocean.app"

# API Key and Device ID you will get after registering your device
API_KEY = "NA"
DEVICE_ID = "NA"


def get_local_ip():
    try:
        # gets IP used for outbound routing
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return None


def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=3).text.strip()
    except:
        return None


def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return int(f.read().strip()) / 1000.0
    except:
        return None


def gather():
    hostname = socket.gethostname()

    payload = {
        "api_key": API_KEY,
        "hostname": hostname,
        "local_ip": get_local_ip(),
        "public_ip": get_public_ip(),
        "cpu_temp": get_cpu_temp(),
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "mem_total_kb": psutil.virtual_memory().total // 1024,
        "mem_used_kb": psutil.virtual_memory().used // 1024,
        "disk_total_kb": psutil.disk_usage('/').total // 1024,
        "disk_used_kb": psutil.disk_usage('/').used // 1024,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z"
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": API_KEY
    }

    try:
        r = requests.post(f"{SERVER}/ping/{DEVICE_ID}", json=payload, headers=headers, timeout=8)
        print(r.status_code, r.text)
    except Exception as e:
        print("Error sending ping:", e)


if __name__ == "__main__":
    gather()