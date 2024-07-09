# AutoSite

AutoSite 是一个人工智能驱动的自动化网站机器人项目，旨在通过人工智能理解需求、编写代码、部署发布。此项目利用 OpenAI 的 GPT-4 模型来实现用户与机器人的交互，并自动处理文件操作和 PowerShell 命令执行。

## 使用方法

### 1. 环境准备

确保你的系统已安装 Python 和 Node.js。

### 2. 克隆 AutoSite 项目

首先，克隆 AutoSite 项目到本地：

```
git clone https://github.com/your-username/autosite.git
cd autosite
```

### 3. 创建新的 GitHub 项目

创建一个新的私有仓库，这将是你的网站项目仓库。

### 4. 在 AutoSite 根目录克隆新项目

在 AutoSite 项目的根目录中，克隆你刚刚创建的新仓库：

```
git clone https://github.com/your-username/your-new-repository.git
```

### 5. Vercel 部署

1. 登录或注册 [Vercel](https://vercel.com/) 账号。
2. 点击"New Project"并选择你刚刚在 GitHub 上创建的新项目（不是 AutoSite 项目）。
3. 按照提示完成项目的部署。
4. 部署完成后，你会获得一个 Vercel 的 URL。

### 6. 配置 Vercel URL 和工作目录

在 AutoSite 项目的 `main.py` 文件中：

1. 更新 `VERCEL_SITE_URL` 变量，将其设置为你的 Vercel URL：

```python
VERCEL_SITE_URL = "https://your-project.vercel.app"
```

2. 更新 `WORKER_DIRECTORY` 变量为你新克隆的项目目录名称：

```python
WORKER_DIRECTORY = "your-new-repository"
```

### 7. 运行程序

在 AutoSite 项目目录中打开终端，执行以下命令：

```
python main.py
```

### 8. 与 AI 交互

程序启动后，你可以与 AI 进行交流，描述你想要实现的网站功能。AI 将自动编写并部署代码到你新创建的项目中，部署成功后会在浏览器中打开你的网站。

## 推荐工具

[Sider](https://sider.ai) - 您的人工智能助手

- Chrome/Edge 扩展
- 无缝集成到日常工作流程
- 提升浏览、阅读和写作效率
- 显著提高工作效率