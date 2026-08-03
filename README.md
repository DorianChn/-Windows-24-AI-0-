# 🤖 Windows 24H AI 助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-green.svg)](https://ollama.com)

**在 Windows 上零成本搭建 24 小时运行的 AI 助手系统**

微信随时问答 · 知识库自动更新 · 本地模型推理 · 崩溃自动恢复

---

## ✨ 功能特性

| 功能 | 效果 |
|------|------|
| 💬 **微信 24h 在线** | 随时发消息问答，秒级响应 |
| 📚 **知识库自动更新** | 每天定时采集 AI/区块链/CS 新闻，自动整理入库 |
| 🧠 **本地模型推理** | Ollama + qwen3:64k，零 API 费用 |
| 🔄 **崩溃自动恢复** | 看门狗 + VBS 自启，7×24 无人值守 |
| ☁️ **云端混合架构** | 本地主力 + 云端备用，成本可控 |
| ⏰ **定时任务系统** | Cron 调度，支持任务链和多平台推送 |
| 📚 **Skills系统** | 55+个实用技能，覆盖编程/学习/职业/效率 |

---

## 📦 项目结构

```
.
├── docs/                    # 文档目录
│   ├── 01-环境搭建.md
│   ├── 02-本地模型部署.md
│   ├── 03-知识库系统.md
│   ├── 04-微信bot部署.md
│   ├── 05-定时任务与自动化.md
│   ├── 06-监控与故障恢复.md
│   ├── 07-云端模型接入.md
│   ├── 08-skills配置指南.md
│   ├── 09-编程学习路径.md
│   └── 10-项目实战指南.md
├── scripts/                 # 实用脚本
│   ├── health-check.py      # 健康检查
│   ├── setup-skills.py      # 配置Skills
│   ├── backup-config.py     # 备份配置
│   ├── restore-config.py    # 恢复配置
│   ├── list-skills.py       # 列出Skills
│   ├── create-project.py    # 创建项目
│   ├── quick-commit.py      # 快速提交
│   ├── update-docs.py       # 更新文档
│   ├── check-env.py         # 检查环境
│   ├── generate-report.py   # 生成报告
│   ├── clean-project.py     # 清理项目
│   ├── deploy-github.py     # 部署到GitHub
│   └── generate-readme.py   # 生成README
├── config-templates/        # 配置模板
│   ├── .env.example
│   └── config.yaml.example
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## 🚀 快速开始

### 环境要求

- Windows 10/11
- NVIDIA GPU（8GB 显存，RTX 3060 起步）
- 16GB 内存
- 50GB 可用磁盘

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/DorianChn/-Windows-24-AI-0-.git
cd -Windows-24-AI-0-

# 2. 检查环境
python scripts/check-env.py

# 3. 安装Ollama
# 从 https://ollama.com 下载安装

# 4. 安装Hermes
pip install hermes-agent

# 5. 配置Hermes
hermes setup

# 6. 配置Skills
python scripts/setup-skills.py
```

---

## 📚 文档目录

| 文档 | 内容 |
|------|------|
| [01 环境搭建](docs/01-环境搭建.md) | Python + Ollama + Hermes 安装 |
| [02 本地模型部署](docs/02-本地模型部署.md) | qwen3:64k 下载、显存管理、性能优化 |
| [03 知识库系统](docs/03-知识库系统.md) | Obsidian + LLM Wiki + Dataview |
| [04 微信 Bot 部署](docs/04-微信bot部署.md) | iLink + Gateway + 防双实例 |
| [05 定时任务与自动化](docs/05-定时任务与自动化.md) | Cron 调度、任务链、纯脚本模式 |
| [06 监控与故障恢复](docs/06-监控与故障恢复.md) | 日志、看门狗、VBS 自启、健康检查 |
| [07 云端模型接入](docs/07-云端模型接入.md) | 阿里云百炼、混合架构、费用控制 |
| [08 Skills配置指南](docs/08-skills配置指南.md) | Skills安装、使用、管理 |
| [09 编程学习路径](docs/09-编程学习路径.md) | 计算机科学与技术专业学习指南 |
| [10 项目实战指南](docs/10-项目实战指南.md) | 项目类型、流程、模板 |

---

## 🔧 实用脚本

```bash
# 健康检查 — 一键检查所有服务状态
python scripts/health-check.py

# 配置Skills — 查看已安装的Skills
python scripts/setup-skills.py

# 备份配置 — 备份Hermes配置
python scripts/backup-config.py

# 恢复配置 — 恢复Hermes配置
python scripts/restore-config.py

# 创建项目 — 创建Python/Web项目模板
python scripts/create-project.py my-project
python scripts/create-project.py my-web-project web

# 快速提交 — 一键提交到GitHub
python scripts/quick-commit.py

# 检查环境 — 检查开发环境
python scripts/check-env.py

# 生成报告 — 生成项目统计报告
python scripts/generate-report.py

# 清理项目 — 清理临时文件
python scripts/clean-project.py

# 部署到GitHub — 部署到GitHub Pages
python scripts/deploy-github.py
```

---

## 💰 成本

| 项目 | 费用 |
|------|------|
| 本地模型推理 | ¥0（Ollama 免费） |
| 云端压缩/辅助 | ~¥0.5/天（阿里云百炼） |
| 硬件 | 已有电脑即可 |
| **总计** | **几乎为零** |

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/xxx`
3. 提交更改：`git commit -m 'add xxx'`
4. 推送分支：`git push origin feature/xxx`
5. 提交 Pull Request

---

## 📄 License

[MIT](LICENSE)

---

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

---

*最后更新: 2026-08-03*
