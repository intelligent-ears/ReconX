import os
import re
from jinja2 import Environment, FileSystemLoader

SEVERITY_COLORS = {
    "critical": "#d32f2f",
    "high": "#f44336",
    "medium": "#ff9800",
    "low": "#ffeb3b",
    "info": "#90caf9"
}

def parse_nuclei_line(line):
    """
    Parse a Nuclei output line to extract severity if possible.
    Example:
    [critical] https://example.com - CVE-2021-1234
    """
    match = re.search(r"\[(critical|high|medium|low|info)\]", line, re.IGNORECASE)
    severity = match.group(1).lower() if match else "info"
    return severity

def generate(domain, output_dir):
    print("[*] Generating HTML report using Jinja2...")

    alive_file = os.path.join(output_dir, "alive.txt")
    nuclei_file = os.path.join(output_dir, "nuclei_report.txt")
    report_file = os.path.join(output_dir, "report.html")

    hosts = []
    if os.path.exists(alive_file):
        with open(alive_file) as f:
            hosts = [line.strip() for line in f if line.strip()]

    vulnerabilities = []
    if os.path.exists(nuclei_file):
        with open(nuclei_file) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                sev = parse_nuclei_line(line)
                vulnerabilities.append({
                    "text": line,
                    "severity": sev,
                    "color": SEVERITY_COLORS.get(sev, "#ccc")
                })

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    html = template.render(
        domain=domain,
        hosts=hosts,
        vulnerabilities=vulnerabilities,
        total_hosts=len(hosts),
        total_vulns=len(vulnerabilities)
    )

    with open(report_file, "w") as f:
        f.write(html)

    print(f"[+] Report generated: {report_file}")
