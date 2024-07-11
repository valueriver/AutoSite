import sqlite3
import json
import os

base_dir = os.path.join(os.getcwd(), 'AI', 'db')  # 修改目录路径

def init_db():
    db_path = os.path.join(base_dir, 'chat.db')
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
        tool_call_id TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conversation_id) REFERENCES conversations (conversation_id)
    )
    ''')

    conn.commit()
    conn.close()

def save_history(conversation_id, messages):
    db_path = os.path.join(base_dir, 'chat.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('INSERT OR IGNORE INTO conversations (conversation_id) VALUES (?)', (conversation_id,))
    
    for message in messages:
        tool_calls = message.get('tool_calls', None)
        tool_call_id = message.get('tool_call_id', None)

        tool_calls_str = json.dumps(tool_calls) if tool_calls is not None else None
        tool_call_id_str = tool_call_id if tool_call_id is not None else None

        cursor.execute('''
            INSERT INTO messages (conversation_id, role, content, tool_calls, tool_call_id) 
            VALUES (?, ?, ?, ?, ?)
        ''', (conversation_id, message['role'], message['content'], tool_calls_str, tool_call_id_str))
    
    conn.commit()
    conn.close()

def load_history(conversation_id):
    db_path = os.path.join(base_dir, 'chat.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT role, content, tool_calls, tool_call_id FROM messages WHERE conversation_id = ? ORDER BY timestamp ASC', (conversation_id,))
    
    messages = []
    for row in cursor.fetchall():
        message = {'role': row[0], 'content': row[1]}
        if row[2]:
            message['tool_calls'] = json.loads(row[2])
        if row[3]:
            message['tool_call_id'] = row[3]
        messages.append(message)
    
    conn.close()
    return messages

def get_conversation_list():
    db_path = os.path.join(base_dir, 'chat.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT conversation_id FROM conversations ORDER BY created_at DESC')
    conversations = [{'conversationId': row[0]} for row in cursor.fetchall()]
    
    conn.close()
    return conversations