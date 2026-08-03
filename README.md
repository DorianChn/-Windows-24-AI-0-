# 🤖 Windows 24H AI 助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Cloud First](https://img.shields.io/badge/Cloud-First-blue.svg)](#cloud-first)

**在 Windows 上低成本搭建 24 小时运行的 AI 助手系统**

☁️ **云端优先** · 微信随时问答 · 知识库自动更新 · 崩溃自动恢复

---

## 🎯 核心理念：Cloud First

> **云端模型为主，本地模型为辅**
> 
> - **云端**：强大、稳定、免维护、按需付费
> - **本地**：备用、离线、隐私保护

| 对比 | 云端模型 | 本地模型 |
|------|---------|---------|
| **性能** | ⭐⭐⭐⭐⭐ 最新最强 | ⭐⭐⭐ 受限于硬件 |
| **稳定性** | ⭐⭐⭐⭐⭐ 99.9%可用 | ⭐⭐⭐ 依赖本地资源 |
| **维护成本** | ⭐⭐⭐⭐⭐ 零维护 | ⭐⭐ 需要GPU/内存 |
| **费用** | ⭐⭐⭐⭐ 按需付费 | ⭐⭐⭐⭐⭐ 一次性投入 |
| **隐私** | ⭐⭐⭐ 云端处理 | ⭐⭐⭐⭐⭐ 本地处理 |

**推荐策略**：
- **主力**：阿里云百炼 deepseek-v4-flash（¥0.2/百万token）
- **压缩/辅助**：deepseek-v4-flash（统一模型，省钱）
- **离线备用**：Ollama + llama3.2:3b（本地免费）

---

## ✨ 功能特性

| 功能 | 效果 |
|------|------|
| ☁️ **云端模型为主** | 阿里云百炼 deepseek-v4-flash，强大稳定 |
| 💬 **微信 24h 在线** | 随时发消息问答，秒级响应 |
| 📚 **知识库自动更新** | 每天定时采集 AI/区块链/CS 新闻，自动整理入库 |
| 🔄 **崩溃自动恢复** | 看门狗 + VBS 自启，7×24 无人值守 |
| ⏰ **定时任务系统** | Cron 调度，支持任务链和多平台推送 |
| 📚 **Skills系统** | 61个实用技能，覆盖编程/学习/研究/职业 |
| 🧠 **本地备用** | Ollama + llama3.2:3b，离线可用 |

---

## 🏗️ 系统架构（云端优先）

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   微信客户端  │ ←→  │  iLink Bot   │ ←→  │ Hermes       │
│             │     │  (协议桥)     │     │ Gateway      │
└─────────────┘     └──────────────┘     └──────┬───────┘
                                                │
                    ┌───────────────────────────┤
                    │                           │
              ┌─────▼──────┐            ┌──────▼───────┐
              │ 阿里云百炼  │            │ Hermes       │
              │ deepseek   │            │ Agent Core   │
              │ v4-flash   │            │ (工具/会话)   │
              │ (云端主力)  │            └──────┬───────┘
              └────────────┘                   │
                    │                          │
                    │ 降级/离线                 │
                    ▼                          │
              ┌────────────┐                   │
              │ Ollama     │                   │
              │ llama3.2   │                   │
              │ (本地备用)  │                   │
              └────────────┘                   │
                                               │
                    ┌───────────────────────────┤
                    │              │            │
              ┌─────▼─────┐  ┌────▼────┐  ┌───▼────────┐
              │ Obsidian  │  │ Cron    │  │ 日志/监控   │
              │ 知识库    │  │ 定时任务│  │ 看门狗     │
              └───────────┘  └─────────┘  └────────────┘
```

---

## ☁️ Cloud First 配置

### 云端模型（主力）

```yaml
# config.yaml
model:
  default: deepseek-v4-flash
  provider: alibaba
  context_length: 65536

providers:
  alibaba:
    base_url: https://ws-d2zlnzz8btbed5od.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
    request_timeout_seconds: 120
    stale_timeout_seconds: 90

compression:
  summary_model: deepseek-v4-flash

auxiliary:
  compression:
    model: deepseek-v4-flash
    provider: alibaba
```

### 本地模型（备用）

```yaml
# config.yaml
fallback_model:
  model: llama3.2:3b
  provider: custom:ollama

custom_providers:
  - name: custom:ollama
    base_url: http://localhost:11434/v1
    model: llama3.2:3b
    models:
      - llama3.2:3b
      - qwen3:64k
```

### 费用对比

| 方案 | 月费用 | 说明 |
|------|--------|------|
| **纯云端** | ¥15-30 | 阿里云百炼，稳定可靠 |
| **云端为主+本地备用** | ¥10-20 | 推荐方案 |
| **纯本地** | ¥0 | 需要GPU，维护成本高 |

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
│   ├── 07-云端模型接入.md      # ⭐ 重点文档
│   ├── 08-skills配置指南.md
│   ├── 09-编程学习路径.md
│   ├── 10-项目实战指南.md
│   └── 11-学术研究Skills.md
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
│   ├── generate-readme.py   # 生成README
│   └── install-research-skills.py  # 安装研究Skills
├── config-templates/        # 配置模板
│   ├── .env.example
│   └── config.yaml.example
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## 🚀 快速开始（云端优先）

### 环境要求

- Windows 10/11
- 16GB 内存
- 50GB 可用磁盘
- **无需GPU**（云端模型为主）

### 三步启动

```bash
# 1. 安装 Hermes
pip install hermes-agent

# 2. 配置云端模型（阿里云百炼）
hermes setup
# 选择 provider: alibaba
# 输入 API key: 你的阿里云百炼API密钥

# 3. 启动 Gateway
hermes gateway run
```

### 详细步骤

```bash
# 克隆仓库
git clone https://github.com/DorianChn/-Windows-24-AI-0-.git
cd -Windows-24-AI-0-

# 检查环境
python scripts/check-env.py

# 配置Skills
python scripts/setup-skills.py

# 健康检查
python scripts/health-check.py
```

---

## 📚 文档目录

| 文档 | 内容 | 重要性 |
|------|------|--------|
| [01 环境搭建](docs/01-环境搭建.md) | Python + Hermes 安装 | ⭐⭐⭐ |
| [02 本地模型部署](docs/02-本地模型部署.md) | Ollama 备用模型 | ⭐⭐ |
| [03 知识库系统](docs/03-知识库系统.md) | Obsidian + LLM Wiki | ⭐⭐⭐ |
| [04 微信 Bot 部署](docs/04-微信bot部署.md) | iLink + Gateway | ⭐⭐⭐ |
| [05 定时任务与自动化](docs/05-定时任务与自动化.md) | Cron 调度 | ⭐⭐⭐ |
| [06 监控与故障恢复](docs/06-监控与故障恢复.md) | 日志、看门狗 | ⭐⭐⭐ |
| [07 云端模型接入](docs/07-云端模型接入.md) | **阿里云百炼配置** | ⭐⭐⭐⭐⭐ |
| [08 Skills配置指南](docs/08-skills配置指南.md) | Skills安装、使用 | ⭐⭐⭐ |
| [09 编程学习路径](docs/09-编程学习路径.md) | CS专业学习指南 | ⭐⭐⭐ |
| [10 项目实战指南](docs/10-项目实战指南.md) | 项目类型、流程 | ⭐⭐⭐ |
| [11 学术研究Skills](docs/11-学术研究Skills.md) | 研究Skills指南 | ⭐⭐⭐ |

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

# 快速提交 — 一键提交到GitHub
python scripts/quick-commit.py

# 检查环境 — 检查开发环境
python scripts/check-env.py

# 安装研究Skills — 安装学术研究Skills
python scripts/install-research-skills.py
```

---

## 💰 成本对比

### 方案一：纯云端（推荐）

| 项目 | 费用 |
|------|------|
| 阿里云百炼 deepseek-v4-flash | ¥0.2/百万token |
| 每天10万token | ¥2/天 |
| **月费** | **¥60** |
| 硬件要求 | 无需GPU |

### 方案二：云端为主+本地备用

| 项目 | 费用 |
|------|------|
| 云端主力 | ¥15-30/月 |
| 本地备用 | ¥0（Ollama免费） |
| **月费** | **¥15-30** |
| 硬件要求 | 可选GPU |

### 方案三：纯本地

| 项目 | 费用 |
|------|------|
| 模型推理 | ¥0 |
| 硬件投入 | ¥3000-5000（GPU） |
| 维护成本 | 高 |
| **月费** | **¥0**（已投入硬件） |

**推荐方案二**：云端为主+本地备用，性价比最高！

---

## 🆚 与其他方案对比

| | 本方案 | ChatGPT Plus | 国产 AI 助手 |
|---|--------|-------------|-------------|
| 月费 | ¥15-60 | ¥140 | ¥30-100 |
| 微信接入 | ✅ | ❌ | 部分支持 |
| 知识库 | ✅ 自动更新 | ❌ | 有限 |
| 云端模型 | ✅ deepseek-v4 | ✅ GPT-4 | ✅ 各家模型 |
| 本地备用 | ✅ Ollama | ❌ | ❌ |
| 自动化任务 | ✅ | ❌ | ❌ |
| 可定制性 | 完全开源 | 闭源 | 闭源 |

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
*核心理念: Cloud First - 云端优先，本地备用*
