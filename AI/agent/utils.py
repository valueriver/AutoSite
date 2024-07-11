import os
import subprocess

def open_browser(url):
    if os.name == 'nt':  # for Windows
        subprocess.Popen(['powershell', '-Command', f'Start-Process "{url}"'])
    else:
        subprocess.Popen(['xdg-open', url])
