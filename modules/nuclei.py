import subprocess
import os

def run(output_dir):
    print("[*] Running Nuclei scan...")
    alive_file = os.path.join(output_dir, "alive.txt")
    nuclei_file = os.path.join(output_dir, "nuclei_report.txt")

    if os.path.exists(alive_file):
        cmd = f"nuclei -l {alive_file} -o {nuclei_file}"
        subprocess.run(cmd, shell=True)
        print(f"[+] Nuclei report saved to {nuclei_file}")
    else:
        print("[!] No alive.txt found — skipping Nuclei.")
