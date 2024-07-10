import os
import json
import subprocess


def get_directory_structure(directory=None):
    if directory is None:
        directory = os.getcwd()

    print(f"[📁读取目录]: {directory}")

    if not os.path.exists(directory):
        return json.dumps({
            "status": "error",
            "message": f"The directory '{directory}' does not exist."
        })
    files = []
    folders = []
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
            elif entry.is_dir():
                folders.append(entry.name)
    return json.dumps({
        "status": "success",
        "structure": {
            "files": files,
            "folders": folders
        }
    })


def write_to_file(data, filename, directory=None):
    if directory is None:
        directory = os.getcwd()

    print(f"[⌨️创建文件]：{filename}")

    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(data)
        return json.dumps({"status": "success", "message": f"Data written to {filepath}"})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})


def read_from_file(filename,  directory=None):
    if directory is None:
        directory = os.getcwd()

    print(f"[💾读取文件]：{filename}")

    filepath = os.path.join(directory, filename)

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = file.read()
        return json.dumps({"status": "success", "data": data})
    except FileNotFoundError:
        return json.dumps({"status": "error", "message": f"{filepath} not found"})


def run_powershell_command(command, directory=None):
    if directory is None:
        directory = os.getcwd()

    print(f"[📟执行命令]：{command}")

    warning = None

    try:
        result = subprocess.run(["powershell", "-Command", command],
                                cwd=directory, capture_output=True, text=True, shell=True)
        return json.dumps({
            "status": "success",
            "output": result.stdout,
            "error": result.stderr,
            "warning": warning
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e),
            "warning": warning
        })


available_functions = {
    "write_to_file": write_to_file,
    "read_from_file": read_from_file,
    "get_directory_structure": get_directory_structure,
    "run_powershell_command": run_powershell_command
}

def RunTools(tool_calls):
    call_messages_list = []
    for tool_call in tool_calls:
        function_name = tool_call['function']['name']
        function_to_call = available_functions.get(function_name)
        if function_to_call:
            function_args = json.loads(tool_call['function']['arguments'])
            function_response = function_to_call(**function_args)
            call_messages_list.append(
                {
                    "tool_call_id": tool_call['id'],
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
    return call_messages_list
