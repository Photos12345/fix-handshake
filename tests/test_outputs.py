import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def report():
    p = Path("/app/report.json")
    assert p.exists(), "/app/report.json not found"
    return json.loads(p.read_text())


def test_total_requests(report):
    """Criterion 1: total_requests is 6."""
    assert report["total_requests"] == 6


def test_unique_ips(report):
    """Criterion 2: unique_ips is 3."""
    assert report["unique_ips"] == 3


def test_top_path(report):
    """Criterion 3: top_path is /index.html."""
    assert report["top_path"] == "/index.html"
