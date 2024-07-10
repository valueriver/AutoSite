from AI.agent.api import ModelApi
from AI.agent.tools import RunTools
from AI.agent.utils import open_browser
from AI.agent.config import tools

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sqlite3
import json

# 设置目录
base_dir = os.path.join(os.getcwd(), 'AI')
web_dir = os.path.join(base_dir, 'web')

# 初始化数据库
def init_db():
    db_path = os.path.join(base_dir, 'chat.db')  # 修改数据库路径到AI目录下
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT,
        role TEXT,
        content TEXT,
        tool_calls TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conversation_id) REFERENCES conversations (conversation_id)
    )
    ''')

    conn.commit()
    conn.close()

init_db()

app = Flask(__name__, static_folder=web_dir, static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message']
    conversation_id = data['conversationId']
    api_key = data['apiKey']
    api_url = data['apiUrl']

    api = ModelApi(api_key, api_url)

    messages = load_history(conversation_id)
    messages.append({"role": "user", "content": user_input})

    while True:
        response = api.oneapi(messages, model="gpt-4o",
                              tools=tools, choices="auto", response_format=None)
        if response['type'] == 'message':
            response_message = response['message']
            messages.append({"role": "assistant", "content": response_message})
            save_history(conversation_id, messages)
            return jsonify({"message": response_message})
        elif response['type'] == 'tools':
            messages.append(response['message'])
            tool_calls = response['tools']
            call_messages_list = RunTools(tool_calls)
            messages.extend(call_messages_list)
            save_history(conversation_id, messages)

@app.route('/chat/list', methods=['GET'])
def chat_list():
    db_path = os.path.join(base_dir, 'chat.db')  # 修改数据库路径到AI目录下
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT conversation_id FROM conversations ORDER BY created_at DESC')
    chat_list = [{'conversationId': row[0]} for row in cursor.fetchall()]
    
    conn.close()
    return jsonify(chat_list)

@app.route('/chat/<conversation_id>', methods=['GET'])
def get_chat(conversation_id):
    messages = load_history(conversation_id)
    return jsonify({'messages': messages})

def save_history(conversation_id, messages):
    db_path = os.path.join(base_dir, 'chat.db')  # 修改数据库路径到AI目录下
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 插入对话记录
    cursor.execute('INSERT OR IGNORE INTO conversations (conversation_id) VALUES (?)', (conversation_id,))
    
    # 插入消息记录
    for message in messages:
        tool_calls = message.get('tool_calls', None)
        cursor.execute('INSERT INTO messages (conversation_id, role, content, tool_calls) VALUES (?, ?, ?, ?)',
                       (conversation_id, message['role'], message['content'], json.dumps(tool_calls)))
    
    conn.commit()
    conn.close()

def load_history(conversation_id):
    db_path = os.path.join(base_dir, 'chat.db')  # 修改数据库路径到AI目录下
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT role, content, tool_calls FROM messages WHERE conversation_id = ? ORDER BY timestamp ASC', (conversation_id,))
    messages = [{'role': row[0], 'content': row[1], 'tool_calls': json.loads(row[2]) if row[2] else None} for row in cursor.fetchall()]
    
    conn.close()
    return messages

if __name__ == "__main__":
    open_browser()
    app.run()
