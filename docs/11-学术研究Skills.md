# 11 学术研究Skills指南

> 基于GitHub热门学术研究Skills整理，覆盖论文全流程

## 六大Skills分类

### 1. AI Research Skills

| Skill | 功能 | 来源 |
|-------|------|------|
| `claude-code` | 代码编写、调试、重构 | Hermes内置 |
| `codex` | OpenAI代码助手 | Hermes内置 |

### 2. Academic Research Skills

| Skill | 功能 | 来源 |
|-------|------|------|
| `literature-review` | 系统性文献综述 | K-Dense-AI/scientific-agent-skills |
| `paper-novelty-design` | 创新点设计 | 自建 |
| `research-proposal` | 研究计划书 | 自建 |

### 3. Scientific Agent Skills

| Skill | 功能 | 来源 |
|-------|------|------|
| `arxiv-digest` | arXiv论文摘要 | zhangzzk/arxiv-digest-skill |
| `scientific-figure` | 科研绘图 | 自建 |
| `citation-management` | 参考文献管理 | K-Dense-AI/scientific-agent-skills |

### 4. Cross Science - AI for Sciences

| Skill | 功能 | 来源 |
|-------|------|------|
| `python-data-analysis` | 数据分析 | 自建 |
| `machine-learning-intro` | 机器学习 | 自建 |

### 5. Drafting Papers

| Skill | 功能 | 来源 |
|-------|------|------|
| `paper-writing` | 论文写作 | 自建 |
| `scientific-figure` | 科研绘图 | 自建 |

### 6. Publication and Review

| Skill | 功能 | 来源 |
|-------|------|------|
| `paper-writing` | 论文写作 | 自建 |
| `citation-management` | 参考文献管理 | K-Dense-AI/scientific-agent-skills |

---

## 推荐GitHub仓库

### 学术研究Skills库

| 仓库 | Stars | Skills数 | 说明 |
|------|-------|---------|------|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 32.4k | 158 | 科学研究Skills库 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | - | 86 | AI研究Skills库 |
| [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) | - | 31 | 学术研究Skills |
| [Imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills) | - | - | 学术研究Skills |

### arXiv相关

| 仓库 | Stars | 说明 |
|------|-------|------|
| [zhangzzk/arxiv-digest-skill](https://github.com/zhangzzk/arxiv-digest-skill) | - | arXiv论文摘要 |
| [aibtcdev/skills/arxiv-research](https://github.com/aibtcdev/skills) | - | arXiv研究Skills |
| [ultimatile/arxiv-skills](https://github.com/ultimatile/arxiv-skills) | - | arXiv Skills |

---

## 安装方法

### 方法1：从GitHub克隆

```bash
# 克隆仓库
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git
cd scientific-agent-skills

# 复制skills到Hermes
cp -r skills/* ~/.hermes/skills/
```

### 方法2：手动创建

```bash
# 使用Hermes创建skill
hermes skills create my-skill
```

### 方法3：使用已有skills

```bash
# 列出已安装skills
hermes skills list

# 查看skill详情
hermes skills view <skill-name>
```

---

## 使用示例

### 1. 文献综述

```
帮我做一篇关于"机器学习在医疗诊断中的应用"的文献综述
```

### 2. 论文创新点

```
帮我分析这个研究方向的创新点
```

### 3. arXiv摘要

```
帮我抓取今天arXiv上关于深度学习的最新论文
```

### 4. 科研绘图

```
帮我画一个实验结果的柱状图
```

### 5. 参考文献

```
帮我整理这些文献的BibTeX格式
```

### 6. 研究计划

```
帮我写一份毕业设计的研究计划书
```

---

## 学术研究工作流

### 完整流程

```
1. 文献调研 (literature-review)
   ↓
2. 创新点设计 (paper-novelty-design)
   ↓
3. 研究计划 (research-proposal)
   ↓
4. 实验实施
   ↓
5. 数据分析 (python-data-analysis)
   ↓
6. 科研绘图 (scientific-figure)
   ↓
7. 论文写作 (paper-writing)
   ↓
8. 参考文献 (citation-management)
   ↓
9. 投稿发表
```

### 每日工作流

```
早上: arxiv-digest (查看最新论文)
上午: 实验/编程
下午: 论文写作
晚上: 文献整理
```

---

## 最佳实践

1. **文献管理** - 使用Zotero/Mendeley
2. **笔记整理** - 使用Obsidian/Notion
3. **版本控制** - 使用Git管理论文
4. **定期备份** - 备份文献和笔记
5. **多读多写** - 每天读论文、写笔记

---

## 常见问题

### Q: Skills安装失败？
A: 检查网络连接，或手动创建skill

### Q: 如何选择Skills？
A: 根据研究阶段选择相应skills

### Q: Skills冲突怎么办？
A: 禁用不需要的skills，保留核心skills

### Q: 如何贡献Skills？
A: Fork仓库，创建skill，提交PR
