import os
import time
import subprocess

def get_info(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return "N/A"

while True:
    os.system('clear')
    print("\033[92m" + "="*50)
    print("      💻 SYSTEM MONITOR - by Jatin")
    print("="*50 + "\033[0m")
    
    uptime = get_info("uptime -p")
    mem = get_info("free -h | awk '/^Mem/{print $3\"/\"$2}'")
    disk = get_info("df -h / | awk 'NR==2{print $3\"/\"$2}'")
    cpu = get_info("top -bn1 | grep 'Cpu' | awk '{print $2}'")
    ip = get_info("hostname -I | awk '{print $1}'")
    user = get_info("whoami")
    
    print(f"\n\033[93m👤 User     :\033[0m {user}")
    print(f"\033[93m⏰ Uptime   :\033[0m {uptime}")
    print(f"\033[93m🧠 CPU      :\033[0m {cpu}% used")
    print(f"\033[93m💾 Memory   :\033[0m {mem}")
    print(f"\033[93m💿 Disk     :\033[0m {disk}")
    print(f"\033[93m🌐 IP       :\033[0m {ip}")
    print("\n\033[90mRefreshing every 2 seconds... Ctrl+C to stop\033[0m")
    print("\033[92m" + "="*50 + "\033[0m")
    
    time.sleep(2)
