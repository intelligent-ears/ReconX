# ReconX

Automated reconnaissance wrapper for Subfinder, Amass, Httpx, and Nuclei.  
Generates clean HTML reports with clickable links and severity-colored vulnerabilities.

## Features
- Subdomain enumeration (Subfinder + Amass)
- Alive host detection (Httpx)
- Vulnerability scanning (Nuclei)
- HTML report with severity colors
- Resume support for interrupted scans

## Requirements
- Go installed
- Python 3.8+
- CLI tools:
  ```bash
  go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
  go install -v github.com/owasp-amass/amass/v4/...@master
  go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
  go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
  ```
## Python packages
  ```bash
  pip install -r requirements.txt
  ```
## Usage
  ```bash
  python3 recon.py -d target.com
  python3 recon.py -d target.com --resume
  python3 recon.py -d target.com --force nuclei
  ```
