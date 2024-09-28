import subprocess
import sys

def install_playwright():
    # Run playwright install command
    subprocess.run([sys.executable, "-m", "playwright", "install"])

if __name__ == "__main__":
    install_playwright()
