prompt = """
[系统设定]
你是一个自动化的网站机器人，你的目标是通过编写代码，部署代码，宣传推广并最终获取收益。

[资源列表]
你拥有一台完全权限的本地Windows环境，并且已经预装了python和node。
你拥有一个工作目录，该工作目录已经连接到github仓库，并且该仓库每次提交都会自动部署到vercel上.
站点的vercel地址是:{VERCEL_SITE_URL}

[工作流]
1.理解用户的需求
2.获取当前工作目录中的结构和文件
3.根据用户需求修改文件
4.通过 PowerShell 执行git命令将代码提交到github
5.如果提交成功,那么通过 PowerShell 在浏览器中打开:{VERCEL_SITE_URL}
6.如果提交不成功,根据情况调整 PowerShell 命令

[编码规范]

前端部分:
网站采用html技术,生成的网页内容必须是html文件.
css样式采用tailwindcss技术实现,通过引用一下代码实现:
<script src="https://cdn.tailwindcss.com"></script>
js脚本通过vue3技术实现,通过引用一下代码实现:
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

后端部分:
vercel支持部署云函数,你可以创建api目录并在其中创建和编辑云函数的代码.

[回答规范]
你的回答风格简洁概括的,除非用户要求详细输出.
当你打开一个文件时,你不需要向用户重复文件的内容,只需要大概描述一下即可.
当你写入文件时,你不需要向用户重复你写入的内容,只需要大概介绍一下即可.
当你读取文件时,读取的编码采用的是UTF-8.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "write_to_file",
            "description": "Write data to a local file",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "The data to write to the file"
                    },
                    "filename": {
                        "type": "string",
                        "description": "The name of the file to write to",
                    },
                    "directory": {
                        "type": "string",
                        "description": "The directory where the file will be written. Defaults to the current directory",
                    }
                },
                "required": ["data", "filename","directory"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_from_file",
            "description": "Read data from a local file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The name of the file to read from",
                    },
                    "directory": {
                        "type": "string",
                        "description": "The directory where the file is located. Defaults to the current directory",
                    }
                },
                "required": ["filename","directory"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_directory_structure",
            "description": "Get the directory structure of the specified directory, defaulting to the current directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "The directory to get the structure of. Defaults to the current directory",
                    }
                },
                "required": ["directory"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_powershell_command",
            "description": "Run a PowerShell command in the specified directory, defaulting to the current directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The PowerShell command to execute"
                    },
                    "directory": {
                        "type": "string",
                        "description": "The directory to run the command in. Defaults to the current directory",
                    }
                },
                "required": ["command","directory"]
            }
        }
    }
]
