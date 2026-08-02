# 🤖 Windows 24H AI 助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-green.svg)](https://ollama.com)

**在 Windows 上零成本搭建 24 小时运行的 AI 助手系统**

微信随时问答 · 知识库自动更新 · 本地模型推理 · 崩溃自动恢复

---

## ✨ 它能做什么

| 功能 | 效果 |
|------|------|
| 💬 **微信 24h 在线** | 随时发消息问答，秒级响应 |
| 📚 **知识库自动更新** | 每天定时采集 AI/区块链/CS 新闻，自动整理入库 |
| 🧠 **本地模型推理** | Ollama + qwen3:64k，零 API 费用 |
| 🔄 **崩溃自动恢复** | 看门狗 + VBS 自启，7×24 无人值守 |
| ☁️ **云端混合架构** | 本地主力 + 云端备用，成本可控 |
| ⏰ **定时任务系统** | Cron 调度，支持任务链和多平台推送 |

## 🏗️ 系统架构

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   微信客户端  │ ←→  │  iLink Bot   │ ←→  │ Hermes       │
│             │     │  (协议桥)     │     │ Gateway      │
└─────────────┘     └──────────────┘     └──────┬───────┘
                                                │
                    ┌───────────────────────────┤
                    │                           │
              ┌─────▼──────┐            ┌──────▼───────┐
              │ Ollama     │            │ Hermes       │
              │ qwen3:64k  │            │ Agent Core   │
              │ (本地推理)  │            │ (工具/会话)   │
              └────────────┘            └──────┬───────┘
                                               │
                    ┌───────────────────────────┤
                    │              │            │
              ┌─────▼─────┐  ┌────▼────┐  ┌───▼────────┐
              │ Obsidian  │  │ Cron    │  │ 日志/监控   │
              │ 知识库    │  │ 定时任务│  │ 看门狗     │
              └───────────┘  └─────────┘  └────────────┘
```

## 📦 技术栈

| 层级 | 组件 | 说明 |
|------|------|------|
| **AI 引擎** | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 开源 AI Agent 框架 |
| **本地模型** | [Ollama](https://ollama.com) + qwen3:64k | 65K 上下文，中文效果好 |
| **云端模型** | 阿里云百炼 deepseek-v4-flash | 压缩/辅助，¥0.2/百万token |
| **微信接入** | iLink Bot | 微信协议桥 |
| **知识库** | Obsidian + LLM Wiki | 结构化知识管理 |
| **定时任务** | Hermes Cron | 自然语言/ Cron 表达式 |
| **监控** | 日志 + 看门狗 + VBS | 崩溃自愈 |

## 🚀 快速开始

### 环境要求

- Windows 10/11
- NVIDIA GPU（8GB 显存，RTX 3060 起步）
- 16GB 内存
- 50GB 可用磁盘

### 三步启动

```bash
# 1. 安装 Ollama + 下载模型
ollama pull qwen3:64k

# 2. 安装 Hermes
pip install hermes-agent

# 3. 配置并启动
hermes setup          # 交互式配置
hermes gateway run    # 启动网关
```

详细步骤见 [docs/](docs/) 目录，从 01 开始按顺序阅读。

## 📖 文档目录

| 文档 | 内容 |
|------|------|
| [01 环境搭建](docs/01-环境搭建.md) | Python + Ollama + Hermes 安装 |
| [02 本地模型部署](docs/02-本地模型部署.md) | qwen3:64k 下载、显存管理、性能优化 |
| [03 知识库系统](docs/03-知识库系统.md) | Obsidian + LLM Wiki + Dataview |
| [04 微信 Bot 部署](docs/04-微信bot部署.md) | iLink + Gateway + 防双实例 |
| [05 定时任务与自动化](docs/05-定时任务与自动化.md) | Cron 调度、任务链、纯脚本模式 |
| [06 监控与故障恢复](docs/06-监控与故障恢复.md) | 日志、看门狗、VBS 自启、健康检查 |
| [07 云端模型接入](docs/07-云端模型接入.md) | 阿里云百炼、混合架构、费用控制 |

## 🔧 实用脚本

```bash
# 健康检查 — 一键检查所有服务状态
python scripts/health-check.py

# Gateway 幂等自启 — 防止双实例
scripts/gateway-service/Hermes_Gateway_Idempotent.vbs
```

## 💰 成本

| 项目 | 费用 |
|------|------|
| 本地模型推理 | ¥0（Ollama 免费） |
| 云端压缩/辅助 | ~¥0.5/天（阿里云百炼） |
| 硬件 | 已有电脑即可 |
| **总计** | **几乎为零** |

## 🆚 与其他方案对比

| | 本方案 | ChatGPT Plus | 国产 AI 助手 |
|---|--------|-------------|-------------|
| 月费 | ¥0~15 | ¥140 | ¥30~100 |
| 微信接入 | ✅ | ❌ | 部分支持 |
| 知识库 | ✅ 自动更新 | ❌ | 有限 |
| 本地运行 | ✅ | ❌ | ❌ |
| 自动化任务 | ✅ | ❌ | ❌ |
| 可定制性 | 完全开源 | 闭源 | 闭源 |

## 🤝 贡献

欢迎提交 Issue 和 PR！

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/xxx`
3. 提交更改：`git commit -m 'add xxx'`
4. 推送分支：`git push origin feature/xxx`
5. 提交 Pull Request

## 📄 License

[MIT](LICENSE)

---

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**
