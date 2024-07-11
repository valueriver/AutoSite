from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from AI.agent.api import ModelApi
from AI.agent.config import tools
from AI.agent.tools import RunTools
from AI.agent.db import init_db, save_history, load_history, get_conversation_list 
from AI.agent.utils import open_browser

import os

# 设置目录
base_dir = os.path.join(os.getcwd(), 'AI')
web_dir = os.path.join(base_dir, 'web')

# 初始化数据库
init_db()

app = Flask(__name__, static_folder=web_dir, static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)


@app.route('/chat/list', methods=['GET'])
def chat_list():
    conversations = get_conversation_list()
    return jsonify(conversations)


@app.route('/chat/<conversation_id>', methods=['GET'])
def get_chat(conversation_id):
    messages = load_history(conversation_id)
    return jsonify({'messages': messages})


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
            tool_messages = RunTools(tool_calls)
            messages.extend(tool_messages)
            save_history(conversation_id, messages)


if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    open_browser(url)
    app.run()
