# AutoSite

AutoSite 是一个人工智能驱动的自动化网站机器人项目，旨在通过人工智能理解需求、编写代码、部署发布。此项目利用 OpenAI 的 GPT-4o 模型来实现用户与机器人的交互，并自动处理文件操作和 PowerShell 命令执行。

## 功能特点

- **自动化代码生成和部署**：用户通过与机器人对话来生成和修改代码，自动提交到 GitHub，并在 Vercel 上部署。
- **文件操作**：支持文件的读取、写入和目录结构的获取。
- **PowerShell 命令执行**：支持在指定目录下运行 PowerShell 命令。

## 使用方法

### 1. 在本地安装 Python 和 Node.js

确保你的系统已安装 Python 和 Node.js。

### 2. 在 GitHub 上创建项目

登录你的 GitHub 账号，创建一个新的私有仓库。你可以在 [GitHub](https://github.com/) 上完成这一步。

### 3. 在 Vercel 上部署该项目

- 登录你的 Vercel 账号，如果没有账号，可以注册一个。
- 点击“New Project”并选择你在 GitHub 上创建的项目。
- 按照提示完成项目的部署。
- 部署完成后，你会获得一个 Vercel 的 URL，将这个 URL 填写到 `config.py` 文件中的 `VERCEL_SITE_URL` 变量中。

### 4. 将 GitHub 的项目克隆到当前目录

打开终端，执行以下命令将项目克隆到本地：

git clone https://github.com/your-username/your-repository.git

### 5. 将全局工作目录 WORKER_DIRECTORY 的 "xxxx" 替换为你克隆在当前目录的目录名称
找到 main.py 文件中的 WORKER_DIRECTORY 变量，并将其中的 "xxxx" 替换为你克隆的项目目录名称。

### 6.在当前目录运行 python main.py
打开终端，进入项目目录，运行以下命令启动程序：
python main.py

### 7.向 AI 交流阐述你想要实现的网站功能
程序启动后，你可以与 AI 进行交流，阐述你想要实现的网站功能。AI 会自动撰写并部署代码，部署成功后将会在浏览器自动打开你的网站。

## 广告推荐

[Sider](https://sider.ai) 是您的人工智能助手，可无缝集成到您的日常工作流程中。它是一个 Chrome/Edge 扩展，使浏览、阅读和写作比以往任何时候都更容易。极大地提高工作效率。
