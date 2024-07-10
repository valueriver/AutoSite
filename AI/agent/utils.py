import os
import json
import subprocess
from AI.agent.config import prompt

HISTORY_DIR = os.path.join(os.getcwd(), 'AI', 'chats')
os.makedirs(HISTORY_DIR, exist_ok=True)

def get_history_file(conversation_id):
    return os.path.join(HISTORY_DIR, f'{conversation_id}.json')

def load_history(conversation_id):
    history_file = get_history_file(conversation_id)
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [{"role": "system", "content": prompt}]

def save_history(conversation_id, messages):
    history_file = get_history_file(conversation_id)
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

def open_browser():
    url = "http://127.0.0.1:5000"
    if os.name == 'nt':  # for Windows
        subprocess.Popen(['powershell', '-Command', f'Start-Process "{url}"'])
    else:
        subprocess.Popen(['xdg-open', url])
