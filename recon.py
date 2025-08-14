#!/usr/bin/env python3
import argparse
import os
import subprocess
import json
from modules import subdomains, probing, nuclei, report

def load_metadata(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {"stages_completed": []}

def save_metadata(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Automated Recon Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--resume", action="store_true", help="Resume from last stage")
    parser.add_argument("--force", nargs='*', help="Force specific stages (comma separated)")
    args = parser.parse_args()

    target_dir = f"output/{args.domain}"
    os.makedirs(target_dir, exist_ok=True)
    metadata_file = os.path.join(target_dir, "metadata.json")

    metadata = load_metadata(metadata_file)

    if "subdomains" not in metadata["stages_completed"] or (args.force and "subdomains" in args.force):
        subdomains.run(args.domain, target_dir)
        metadata["stages_completed"].append("subdomains")
        save_metadata(metadata_file, metadata)
    elif args.resume:
        print("[*] Skipping subdomains (resume mode)")

    if "alive_hosts" not in metadata["stages_completed"] or (args.force and "alive_hosts" in args.force):
        probing.run(target_dir)
        metadata["stages_completed"].append("alive_hosts")
        save_metadata(metadata_file, metadata)
    elif args.resume:
        print("[*] Skipping alive hosts (resume mode)")
        
    if "nuclei" not in metadata["stages_completed"] or (args.force and "nuclei" in args.force):
        nuclei.run(target_dir)
        metadata["stages_completed"].append("nuclei")
        save_metadata(metadata_file, metadata)
    elif args.resume:
        print("[*] Skipping Nuclei (resume mode)")

    report.generate(args.domain, target_dir)

if __name__ == "__main__":
    main()
