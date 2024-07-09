# 使用方法:
# 1. 在本地安装Python和Node.js
# 2. 在GitHub上创建项目
# 3. 在Vercel上部署该项目
#    部署完成后，你会获得一个Vercel的URL，将这个URL填写到下面的`VERCEL_SITE_URL`变量中。
# 4. 将Vercel部署后的地址填写到`VERCEL_SITE_URL`变量
# 5. 将GitHub的项目克隆到当前目录 
# 6. 将全局工作目录`WORKER_DIRECTORY`的"xxxx"替换为你克隆在当前目录的目录名称
# 7. 在当前目录运行python main.py
# 8. 向AI交流阐述你想要实现的网站功能
#    程序启动后，你可以与AI进行交流，阐述你想要实现的网站功能。AI会自动撰写并部署代码,部署成功后将会在浏览器自动打开你的网站

from agent.model import OpenAIAPI
from agent.tools import run_tools
from agent.config import prompt, tools

import os

# openai api key
API_KEY = 'sk-xxxx'
# openai api url
API_URL = 'https://xxxx/v1/chat/completions'
# 你克隆的项目的目录名称，例如你创建的项目叫GPT5，那么克隆完成后就会有一个GPT5的目录，这里就填写GPT5
WORKER_DIRECTORY = os.path.join(os.getcwd(), "xxxx")
# 部署在vercel的网站地址
VERCEL_SITE_URL = 'https://xxxx.vercel.app'

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
                call_messages_list = run_tools(tool_calls, WORKER_DIRECTORY)
                messages.extend(call_messages_list)

if __name__ == "__main__":
    run()
