from agent.model import OpenAIAPI
from agent.tools import run_tools
from agent.config import prompt, tools

import os

# 从环境变量中获取OpenAI API密钥
API_KEY = os.getenv('OPENAI_API_KEY')
# 从环境变量中获取OpenAI API URL
API_URL = os.getenv('OPENAI_API_URL')
# 从环境变量中获取克隆的项目的目录名称
GIT_DIRECTORY = os.path.join(os.getcwd(), os.getenv('GIT_DIRECTORY'))
# 从环境变量中获取部署在vercel的网站地址
VERCEL_SITE_URL = os.getenv('VERCEL_SITE_URL')

def run():
    prompt_content = prompt.replace("{VERCEL_SITE_URL}", VERCEL_SITE_URL)
    messages = [{"role": "system", "content": prompt_content}]
    api = OpenAIAPI(API_KEY, API_URL)

    while True:
        user_input = input("👤: ")
        messages.append({"role": "user", "content": user_input})
        while True:
            response = api.oneapi(messages, model="gpt-4o", tools=tools, choices="auto", response_format=None)
            if response['type'] == 'message':
                response_message = response['message']
                print("🤖:", response_message)
                messages.append({"role": "assistant", "content": response_message})
                break  
            elif response['type'] == 'tools':
                messages.append(response['message'])
                tool_calls = response['tools']
                call_messages_list = run_tools(tool_calls, GIT_DIRECTORY)
                messages.extend(call_messages_list)

if __name__ == "__main__":
    run()
