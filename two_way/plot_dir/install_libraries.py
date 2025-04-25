# filename: install_libraries.py
import sys

def install(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

libraries = ['yfinance', 'pandas', 'matplotlib']

for library in libraries:
    try:
        __import__(library)
    except ImportError:
        install(library)