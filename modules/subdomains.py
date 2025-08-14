import subprocess
import os

def run(domain, output_dir):
    print(f"[*] Running Subfinder for {domain}...")
    subfinder_file = os.path.join(output_dir, "subfinder.txt")
    subprocess.run(f"subfinder -d {domain} -o {subfinder_file}", shell=True)

    print(f"[*] Running Amass for {domain}...")
    amass_file = os.path.join(output_dir, "amass.txt")
    subprocess.run(f"amass enum -passive -d {domain} -o {amass_file}", shell=True)

    print("[*] Merging results...")
    all_subs = set()
    for file in [subfinder_file, amass_file]:
        if os.path.exists(file):
            with open(file) as f:
                for line in f:
                    all_subs.add(line.strip())

    merged_file = os.path.join(output_dir, "subdomains.txt")
    with open(merged_file, "w") as f:
        for sub in sorted(all_subs):
            f.write(sub + "\n")

    print(f"[+] Found {len(all_subs)} unique subdomains.")
