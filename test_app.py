import subprocess
import sys

def test_app_runs():
    result = subprocess.run([sys.executable, "app.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, Jenkins!" in result.stdout
