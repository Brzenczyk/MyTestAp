import subprocess

def test_button1():
    result = subprocess.run(["MyTest.exe", "button1"], capture_output=True, text=True)
    assert "IPv4 Info" in result.stdout
