"""Exporters for bomb output."""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path

from .models import Scope


# ----------------- Exporting -----------------

def export_csv(scope: Scope, outdir: Path) -> None:
    """
    Export simple CSVs. Later: richer exports (Markdown, PlexTrac JSON, etc.).
    """
    outdir.mkdir(parents=True, exist_ok=True)
    domains_csv = outdir / "domains.csv"
    hosts_csv = outdir / "hosts.csv"
    findings_csv = outdir / "findings.csv"

    logging.info("Exporting CSV to %s", outdir)

    # Domains
    with domains_csv.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "source", "ips"])
        for d in scope.domains:
            writer.writerow([d.name, d.source, ";".join(d.ips)])

    # Hosts
    with hosts_csv.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "domains"])
        for h in scope.hosts:
            writer.writerow([h.ip, ";".join(h.domains)])

    # Findings
    with findings_csv.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["type", "target", "data_json"])
        for fl in scope.findings:
            writer.writerow([fl.type, fl.target, json.dumps(fl.data)])


def export_html(scope: Scope, outdir: Path) -> None:
    """
    Very minimal HTML report skeleton. You can replace this with Jinja2 later.
    """
    outdir.mkdir(parents=True, exist_ok=True)
    html_path = outdir / "report.html"
    logging.info("Exporting HTML report to %s", html_path)

    with html_path.open("w") as f:
        f.write("<html><head><title>bomb report</title></head><body>\n")
        f.write(f"<h1>bomb report for {scope.seed}</h1>\n")

        f.write("<h2>Domains</h2><ul>\n")
        for d in scope.domains:
            f.write(f"<li>{d.name} (source: {d.source})</li>\n")
        f.write("</ul>\n")

        f.write("<h2>Hosts</h2><ul>\n")
        for h in scope.hosts:
            f.write(f"<li>{h.ip} ({', '.join(h.domains)})</li>\n")
        f.write("</ul>\n")

        f.write("<h2>Findings</h2><ul>\n")
        for fl in scope.findings:
            f.write(
                f"<li><strong>{fl.type}</strong> on {fl.target}: "
                f"<pre>{json.dumps(fl.data, indent=2)}</pre></li>\n"
            )
        f.write("</ul>\n")

        f.write("</body></html>\n")
