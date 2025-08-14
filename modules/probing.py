import subprocess
import os

def run(output_dir):
    print("[*] Probing for alive hosts...")
    subs_file = os.path.join(output_dir, "subdomains.txt")
    alive_file = os.path.join(output_dir, "alive.txt")
    subprocess.run(f"httpx -l {subs_file} -o {alive_file}", shell=True)
    print(f"[+] Alive hosts saved to {alive_file}")
