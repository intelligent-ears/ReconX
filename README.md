# ReconX

**ReconX** is an automated reconnaissance framework for bug bounty hunters and penetration testers.  
It integrates multiple tools for **subdomain enumeration**, **live host discovery**, **vulnerability scanning**, and **archived URL collection**, with a final **HTML report** generated for easy review.

---

## Features

- **Subdomain Enumeration**  
  Uses:
  - [`subfinder`](https://github.com/projectdiscovery/subfinder)  
  - [`amass`](https://github.com/owasp-amass/amass)

- **Live Host Discovery**  
  Uses:
  - [`httpx`](https://github.com/projectdiscovery/httpx)

- **Vulnerability Scanning**  
  Uses:
  - [`nuclei`](https://github.com/projectdiscovery/nuclei)

- **Archived URL Discovery**  
  Uses:
  - [`waybackurls`](https://github.com/tomnomnom/waybackurls)  
  - [`gau`](https://github.com/lc/gau)

- **Report Generation**  
  Uses:
  - [`Jinja2`](https://jinja.palletsprojects.com/) for clean, color-coded HTML reports.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/intelligent-ears/ReconX.git
cd ReconX
```
# Install dependencies
```bash
sudo apt install subfinder amass httpx nuclei waybackurls gau
pip install -r requirements.txt```
```
## Usage
```bash
python3 recon.py -d example.com -o output_dir
```
# This will:
1. Enumerate subdomains with Subfinder & Amass
2. Probe live hosts with Httpx
3. Scan vulnerabilities with Nuclei
4. Fetch archived URLs with Waybackurls & GAU
5. Generate an HTML report in the output directory
