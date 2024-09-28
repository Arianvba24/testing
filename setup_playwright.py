import os

def install_playwright():
    os.system('playwright install')
    os.system('playwright install-deps')

if __name__ == "__main__":
    install_playwright()
