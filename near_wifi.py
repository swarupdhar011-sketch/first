import subprocess

def scan_wifi():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )
        print(result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    scan_wifi()
