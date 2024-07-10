# AutoSite

AutoSite 是一个人工智能驱动的自动化网站机器人项目，旨在通过人工智能理解需求、编写代码、部署发布。此项目利用 OpenAI 的 GPT-4 模型来实现用户与机器人的交互，并自动处理文件操作和 PowerShell 命令执行。

## 示例效果

需求描述：实现一个对话网站，前端一个按钮，点击后请求后端，显示后端返回的笑话内容。

### 对话
![自动化部署示例](https://pub-20abb0d076b24b52a65a8f98d262b891.r2.dev/20240710101436.png)

### 效果
![自动化部署示例](https://pub-20abb0d076b24b52a65a8f98d262b891.r2.dev/20240710102338.png)

## 使用方法

### 1. 环境准备

确保你的系统已安装 Python 

如果想让ai编写后端api，那么需要安装Node

### 2. 克隆 AutoSite 项目

首先，克隆 AutoSite 项目到本地：

```
git clone https://github.com/valueriver/AutoSite
cd AutoSite
```

### 3. 创建新的 GitHub 项目

创建一个新的私有仓库，仓库中创建一个基础的index.html文件，里面可以随便写点内容，例如：hello world。仓库中创建一个空的api目录，该目录用于部署后端云函数的目录。

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

### 6. 配置环境变量

1.API_KEY和API_URL即openai的apikey和apiurl，如果你暂时没有这些，你可以联系我的微信来购买：WoodChangeLY    
2.GIT_DIRECTORY是你新建的github项目克隆在当前文件夹的目录名，例如，如果你的项目是gpt5，那么克隆在当前目录后，就会有一个gpt5的目录，那么就把GIT_DIRECTORY设置为gpt5  
3.VERCEL_SITE_URL是你在vercel部署网站后vercel提供给你的网站在线访问地址。   

### 7. 运行程序

在 AutoSite 项目目录中打开终端，执行以下命令：

```
python main.py
```

### 8. 与 AI 交互

程序启动后，你可以与 AI 进行交流，描述你想要实现的网站功能。AI 将自动编写并部署代码到你新创建的项目中，部署成功后会在浏览器中打开你的网站。

## 问题&交流

v: WoodChangeLY

## 推荐工具

[Sider](https://sider.ai) - 您的人工智能助手

- Chrome/Edge 扩展
- 无缝集成到日常工作流程
- 提升浏览、阅读和写作效率
- 显著提高工作效率
