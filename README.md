# Hermes AI 助手部署指南

> 在 Windows 10 上零成本搭建 24 小时运行的 AI 助手系统

## 效果

- 微信 24 小时在线 AI 助手，随时问答
- 自动定时更新知识库（每天定时采集、整理、入库）
- 本地模型推理，零 API 费用
- 崩溃自动恢复，无需人工干预

## 技术栈

| 组件 | 选型 | 用途 |
|------|------|------|
| AI Agent | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 核心对话引擎 |
| 本地模型 | Ollama + qwen3:64k | 推理，零费用 |
| 微信接入 | iLink Bot | 微信消息收发 |
| 知识库 | Obsidian + LLM Wiki | 结构化知识管理 |
| 定时任务 | Hermes Cron | 自动化采集更新 |
| 监控 | 日志 + 看门狗 + VBS 自启 | 7×24 稳定运行 |

## 硬件要求

- Windows 10/11
- NVIDIA GPU（8GB 显存即可，RTX 3060 起步）
- 16GB 内存
- 50GB 可用磁盘

## 项目结构

```
hermes-ai-deploy-guide/
├── README.md                  ← 你在这里
├── docs/
│   ├── 01-环境搭建.md
│   ├── 02-本地模型部署.md
│   ├── 03-知识库系统.md
│   ├── 04-微信bot部署.md
│   ├── 05-定时任务与自动化.md
│   └── 06-监控与故障恢复.md
├── scripts/
│   ├── gateway-service/
│   │   └── Hermes_Gateway_Idempotent.vbs
│   └── health-check.py
└── config-templates/
    ├── config.yaml.example
    └── .env.example
```

## 快速开始

按顺序阅读 docs/ 下的 6 篇文档，从 01 开始。

## 环境验证

```bash
# 检查 Python
python --version  # 需要 3.10+

# 检查 Ollama
ollama list

# 检查 GPU
nvidia-smi

# 检查 Hermes
hermes --version
```

## License

MIT
