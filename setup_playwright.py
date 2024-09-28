import subprocess
import sys

def install_playwright():
    # This command installs all required browsers (Chromium, Firefox, WebKit)
    subprocess.run([sys.executable, "-m", "playwright", "install", "--with-deps"])

if __name__ == "__main__":
    install_playwright()
