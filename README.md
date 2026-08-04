# 🤖 Windows 24H AI 助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Cloud First](https://img.shields.io/badge/Cloud-First-blue.svg)](#-cloud-first-架构)

> **在 Windows 上低成本搭建 24 小时运行的 AI 助手系统**
>
> ☁️ 云端优先 · 💬 微信随时问答 · 📚 知识库自动更新 · 🔄 崩溃自动恢复

---

## 📋 项目简介

这是一个基于 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 的 **云端优先** AI 助手系统，专为 Windows 用户设计。

**核心特点：**

- ✅ **云端模型主力** - 阿里云百炼 deepseek-v4-flash，强大稳定
- ✅ **本地模型备用** - Ollama + llama3.2:3b，离线可用
- ✅ **7×24 无人值守** - 部署到服务器，永不掉线
- ✅ **微信随时问答** - 随时发消息，秒级响应
- ✅ **知识库自动更新** - 每天定时采集最新资讯
- ✅ **成本极低** - 月费仅 ¥65-130，比 ChatGPT Plus 优惠 10 倍

---

## 🎯 为什么选择这个方案？

### 痛点分析

| 问题 | 本方案 | ChatGPT Plus | 国产 AI 助手 |
|------|--------|--------------|--------------|
| 月费 | 65-130 元 | 140 元 | 30-100 元 |
| 微信接入 | ✅ | ❌ | 部分支持 |
| 知识库 | ✅ 自动更新 | ❌ | 有限 |
| 云端模型 | ✅ deepseek-v4 | ✅ GPT-4 | ✅ 各家模型 |
| 本地备用 | ✅ Ollama | ❌ | ❌ |
| 自动化任务 | ✅ | ❌ | ❌ |
| 可定制性 | 完全开源 | 闭源 | 闭源 |
| 7×24 运行 | ✅ | ❌ | ❌ |

### 费用对比

| 方案 | 服务器 | 模型 | 月费总计 | 适合场景 |
|------|--------|------|----------|----------|
| 云端主导 | 50-100 元 | 15-30 元 | 65-130 元 | 生产环境、7×24 |
| 本地主导 | ¥0 | 15-30 元 | 15-30 元 | 开发测试 |
| 纯本地 | ¥0 | ¥0 | ¥0 | 隐私敏感 |

---

## 🏗️ 云优先架构

### 系统架构图

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   微信客户端  │ ←→  │  iLink Bot   │ ←→  │   Hermes     │
│             │     │  (协议桥)     │     │   Gateway    │
└─────────────┘     └──────────────┘     └──────┬───────┘
                                                │
                    ┌───────────────────────────┤
                    │                           │
              ┌─────▼──────┐            ┌──────▼───────┐
              │  阿里云百炼  │            │   Hermes     │
              │  deepseek   │            │   Agent Core │
              │  v4-flash   │            │  (工具/会话)  │
              │  (云端主力)  │            └──────┬───────┘
              └────────────┘                   │
                    │                          │
                    │ 降级/离线                 │
                    ▼                          │
              ┌────────────┐                   │
              │   Ollama   │                   │
              │  llama3.2  │                   │
              │  (本地备用) │                   │
              └────────────┘                   │
                                               │
                    ┌───────────────────────────┤
                    │              │            │
              ┌─────▼─────┐  ┌────▼────┐  ┌───▼────────┐
              │  Obsidian  │  │  Cron   │  │  日志/监控  │
              │   知识库   │  │ 定时任务│  │   看门狗    │
              └───────────┘  └─────────┘  └────────────┘
```

### 架构说明

| 组件 | 作用 | 优先级 |
|------|------|--------|
| 阿里云百炼 | 云端模型，主力推理 | ⭐⭐⭐⭐⭐ |
| Ollama | 本地模型，备用降级 | ⭐⭐⭐ |
| iLink Bot | 微信协议桥 | ⭐⭐⭐⭐⭐ |
| Hermes Agent | AI 核心，工具调用 | ⭐⭐⭐⭐⭐ |
| Obsidian | 知识库管理 | ⭐⭐⭐⭐ |
| Cron | 定时任务调度 | ⭐⭐⭐⭐ |

---

## ✨ 功能特点

### 💬 微信 24 小时在线

- **问答** - 随时发消息，秒级响应
- **多平台支持** - 微信、Telegram、Discord 等
- **智能回复** - 支持文字、图片、文件等
- **上下文记忆** - 支持多轮对话，记住上下文

### ☁️ 云端模型主力

- **阿里云百炼** - deepseek-v4-flash，稳定可靠
- **按量付费** - ¥0.2/百万 token，性价比极高
- **免维护** - 不消耗 GPU，不消耗本地资源
- **自动降级** - 云端不可用时自动切换到本地

### 📚 知识库自动更新

- **定时采集** - 每天自动采集 AI/区块链/CS 资讯
- **结构化存储** - Obsidian + LLM Wiki
- **智能整理** - 自动分类、打标签、建链接
- **多知识库** - 支持多个独立知识库

### 🔄 崩溃自动恢复

- **看门狗** - 自动检测服务状态
- **自动重启** - 崩溃后自动恢复
- **VBS 自启动** - 开机自动启动
- **健康检查** - 定期检查系统状态

### ⏰ 定时任务系统

- **Cron 调度** - 支持自然语言和 Cron 表达式
- **任务链** - 支持任务依赖和上下文传递
- **多平台投递** - 微信、Telegram、Discord 等
- **纯脚本模式** - 支持无 Agent 的脚本任务

### 📚 技能系统

- **61 个实用技能** - 覆盖编程、学习、研究、职场
- **学术研究技能** - 文献综述、论文写作、科研绘图
- **编程开发技能** - 数据分析、机器学习、Web 开发
- **自动加载** - 根据上下文自动加载相关技能

---

## 🚀 快速开始

### 方案一：本地部署（推荐入门）

**适合：** 学习、开发、测试

```bash
# 1. 安装 Hermes
pip install hermes-agent

# 2. 配置云端模型（阿里云百炼）
hermes setup
# 选择 provider: alibaba
# 输入 API key: 你的阿里云百炼 API 密钥

# 3. 启动 Gateway
hermes gateway run
```

**费用：** ¥15-30/月（仅模型费用）

### 方案二：服务器部署（推荐生产）

**适合：** 7×24 无人值守、生产环境

```bash
# 1. 购买阿里云 ECS 服务器（2核2G ¥50/月）
# 2. 一键部署脚本
bash scripts/server-setup.sh

# 3. 配置微信 Bot
# 参考 docs/04-微信bot部署.md
```

**费用：** ¥65-130/月（服务器+模型）

### 方案三：纯本地部署

**适合：** 隐私敏感、离线环境

```bash
# 1. 安装 Ollama
# 从 https://ollama.com 下载

# 2. 下载模型
ollama pull llama3.2:3b

# 3. 安装 Hermes
pip install hermes-agent

# 4. 配置本地模型
hermes setup
# 选择 provider: custom:ollama
```

**费用：** ¥0（纯免费）

---

## 📦 项目结构

```
.
├── docs/                    # 文档目录（14 个文档）
│   ├── 01-环境搭建.md
│   ├── 02-本地模型部署.md
│   ├── 03-知识库系统.md
│   ├── 04-微信bot部署.md
│   ├── 05-定时任务与自动化.md
│   ├── 06-监控与故障恢复.md
│   ├── 07-云端模型接入.md
│   ├── 08-skills配置指南.md
│   ├── 09-编程学习路径.md
│   ├── 10-项目实战指南.md
│   ├── 11-学术研究Skills.md
│   └── 12-服务器部署指南.md
├── scripts/                 # 实用脚本（20 个脚本）
│   ├── health-check.py      # 健康检查
│   ├── setup-skills.py      # 配置 Skills
│   ├── backup-config.py     # 备份配置
│   ├── restore-config.py    # 恢复配置
│   ├── list-skills.py       # 列出 Skills
│   ├── create-project.py    # 创建项目
│   ├── quick-commit.py      # 快速提交
│   ├── update-docs.py       # 更新文档
│   ├── check-env.py         # 检查环境
│   ├── generate-report.py   # 生成报告
│   ├── clean-project.py     # 清理项目
│   ├── deploy-github.py     # 部署到 GitHub
│   ├── generate-readme.py   # 生成 README
│   ├── install-deps.py      # 安装依赖
│   ├── run-tests.py         # 运行测试
│   ├── format-code.py       # 格式化代码
│   ├── check-security.py    # 安全检查
│   ├── install-research-skills.py  # 安装研究 Skills
│   ├── server-setup.sh      # 服务器部署
│   └── server-manage.sh     # 服务器管理
├── config-templates/        # 配置模板
│   ├── .env.example
│   └── config.yaml.example
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## 📚 文档目录

### 基础篇（必读）

| 文档 | 内容 | 重要性 |
|------|------|--------|
| 01 环境搭建 | Python + Hermes 安装 | ⭐⭐⭐ |
| 02 本地模型部署 | Ollama 备用模型 | ⭐⭐ |
| 03 知识库系统 | Obsidian + LLM Wiki | ⭐⭐⭐ |
| 04 微信机器人部署 | iLink + Gateway | ⭐⭐⭐ |

### 进阶篇（推荐）

| 文档 | 内容 | 重要性 |
|------|------|--------|
| 05 定时任务与自动化 | Cron 调度 | ⭐⭐⭐ |
| 06 监控与故障恢复 | 日志、看门狗 | ⭐⭐⭐ |
| 07 云端接入 | 阿里云百炼配置 | ⭐⭐⭐⭐⭐ |
| 08 技能配置指南 | 技能安装、使用 | ⭐⭐⭐ |

### 高级篇（任选）

| 文档 | 内容 | 重要性 |
|------|------|--------|
| 09 编程学习路径 | CS 专业学习指南 | ⭐⭐⭐ |
| 10 项目实战指南 | 项目类型、流程 | ⭐⭐⭐ |
| 11 学术研究技能 | 研究技能指南 | ⭐⭐⭐ |
| 12 服务器部署指南 | 7×24 小时部署 | ⭐⭐⭐⭐⭐ |

---

## 🔧 实用脚本

### 基础脚本

```bash
# 健康检查 — 一键检查所有服务状态
python scripts/health-check.py

# 配置 Skills — 查看已安装的 Skills
python scripts/setup-skills.py

# 检查环境 — 检查开发环境
python scripts/check-env.py
```

### 项目管理

```bash
# 创建项目 — 创建 Python/Web 项目模板
python scripts/create-project.py my-project

# 快速提交 — 一键提交到 GitHub
python scripts/quick-commit.py

# 生成报告 — 生成项目统计报告
python scripts/generate-report.py
```

### 服务器管理

```bash
# 服务器部署 — 一键部署到服务器
bash scripts/server-setup.sh

# 服务器管理 — 管理服务器状态
bash scripts/server-manage.sh status
bash scripts/server-manage.sh start
bash scripts/server-manage.sh restart
bash scripts/server-manage.sh logs
```

---

## 💰 费用详细分析

### 方案一：纯云端（推荐入门）

| 项目 | 费用 |
|------|------|
| 阿里云百炼 deepseek-v4-flash | ¥0.2/百万 token |
| 每天 10 万 token | ¥2/天 |
| 月费 | ¥60 |
| 硬件要求 | 无 |

### 方案二：云端主 + 本地备用（推荐生产）

| 项目 | 费用 |
|------|------|
| 云端主力 | 15-30 元/月 |
| 本地备用 | ¥0（Ollama 免费） |
| 月费 | 15-30 元 |
| 硬件要求 | 任意 GPU |

### 方案三：服务器部署（推荐 7×24）

| 项目 | 费用 |
|------|------|
| 阿里云 ECS 2核2G | ¥50/月 |
| 阿里云百炼 | ¥15/月 |
| 月费 | ¥65 |
| 硬件要求 | 无 |

### 方案四：纯本地（推荐隐私）

| 项目 | 费用 |
|------|------|
| 模型推理 | ¥0 |
| 硬件投入 | ¥3000-5000（GPU） |
| 维护成本 | 高 |
| 月费 | ¥0（已投入硬件） |

---

## 🆚 与其他方案对比

### 功能对比

| 功能 | 本方案 | ChatGPT Plus | 国产 AI 助手 |
|------|--------|--------------|--------------|
| 微信接入 | ✅ | ❌ | 部分支持 |
| 知识库 | ✅ 自动更新 | ❌ | 有限 |
| 云端模型 | ✅ deepseek-v4 | ✅ GPT-4 | ✅ 各家模型 |
| 本地备用 | ✅ Ollama | ❌ | ❌ |
| 自动化任务 | ✅ | ❌ | ❌ |
| 可定制性 | 完全开源 | 闭源 | 闭源 |
| 7×24 运行 | ✅ | ❌ | ❌ |

### 费用对比

| 方案 | 月费 | 年费 | 节省开支 |
|------|------|------|----------|
| 本方案 | 65-130 元 | ¥780-1560 | - |
| ChatGPT Plus | 140 元 | ¥1680 | ¥900-1100 |
| 国产 AI 助手 | 30-100 元 | ¥360-1200 | ¥0-420 |

**结论：本方案性价比最高，功能最全！**

---

## 🛠️ 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| AI 引擎 | Hermes Agent | 开源 AI Agent 框架 |
| 云端模型 | 阿里云百炼 | deepseek-v4-flash |
| 本地模型 | Ollama | llama3.2:3b |
| 微信接入 | iLink Bot | 微信协议桥 |
| 知识库 | Obsidian + LLM Wiki | 结构化知识管理 |
| 定时任务 | Hermes Cron | 自然语言 / Cron 表达式 |
| 监控 | 日志 + 看门狗 + VBS | 崩溃自愈 |

---

## 🔗 相关项目

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - AI Agent 框架
- [Ollama](https://ollama.com) - 本地大模型运行
- [Obsidian](https://obsidian.md) - 知识管理工具
- [iLink Bot](https://github.com/nicepkg/ilink-bot) - 微信协议桥

---

## 📞 联系方式

- **GitHub:** [@DorianChn](https://github.com/DorianChn)
- **Email:** 3671276527@qq.com

---

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

## 🙏 致谢

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - 提供 AI Agent 框架
- [阿里云百炼](https://dashscope.aliyun.com) - 提供云端模型服务
- [Ollama](https://ollama.com) - 提供本地模型运行环境

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=DorianChn/-Windows-24-AI-0-&type=Date)](https://star-history.com/#DorianChn/-Windows-24-AI-0-&Date)

---

<div align="center">

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

</div>
