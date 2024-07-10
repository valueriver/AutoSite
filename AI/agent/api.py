import requests
import json

class ModelApi:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def oneapi(self, messages, model=None, tools=None, choices="auto", response_format=None):
        body = {
            "messages": messages,
            "temperature": 0,
        }

        if model:
            body["model"] = model
        else:
            body["model"] = 'gpt-4o'

        if tools:
            body["tools"] = tools
            body["tool_choice"] = choices

        if response_format:
            body["response_format"] = response_format

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(self.api_url, headers=headers, data=json.dumps(body))

        if response.status_code != 200:
            print(response.text)

        data = response.json()

        try:
            if data['choices'][0]['finish_reason'] == 'stop':
                return {
                    'type': 'message',
                    'message': data['choices'][0]['message']['content']
                }
            else:
                return {
                    'type': 'tools',
                    'message': data['choices'][0]['message'],
                    'tools': data['choices'][0]['message'].get('tool_calls', [])
                }
        except Exception as error:
            return {
                'type': 'error',
                'message': str(error)
            }
