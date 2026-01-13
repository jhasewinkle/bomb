"""
bomb data models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Domain:
    name: str
    source: str = "seed"  # seed / amass / crtsh / dnsdumpster / etc.
    ips: List[str] = field(default_factory=list)


@dataclass
class Host:
    ip: str
    domains: List[str] = field(default_factory=list)


@dataclass
class Finding:
    """Generic finding object; specialize later (service, vuln, leak, etc.)."""

    type: str
    target: str
    data: dict


@dataclass
class Scope:
    seed: str  # original domain or IP
    domains: List[Domain] = field(default_factory=list)
    hosts: List[Host] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)
