import subprocess
import sys


def test_cli_calc():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "10+8*2"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "26.0"


def test_cli_convert():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "convert",
            "100",
            "--from",
            "cm",
            "--to",
            "m",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "1.0"
