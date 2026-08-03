# 08 Skills配置指南

> 为大一新生（计算机科学与技术）定制的Skills配置

## 推荐Skills

### 编程学习类

| Skill | 功能 | 安装命令 |
|-------|------|----------|
| `python-data-analysis` | pandas/numpy数据处理 | `hermes skills install programming/python-data-analysis` |
| `machine-learning-intro` | sklearn模型训练 | `hermes skills install programming/machine-learning-intro` |
| `web-development` | HTML/CSS/JS + Flask | `hermes skills install programming/web-development` |
| `algorithm-practice` | LeetCode刷题模板 | `hermes skills install study/algorithm-practice` |
| `database-operations` | MySQL/SQLite操作 | `hermes skills install programming/database-operations` |

### 学习效率类

| Skill | 功能 | 安装命令 |
|-------|------|----------|
| `study-notes-workbench` | 学习笔记管理 | `hermes skills install productivity/study-notes-workbench` |
| `paper-writing` | 论文写作LaTeX | `hermes skills install study/paper-writing` |
| `exam-preparation` | 考试复习计划 | `hermes skills install study/exam-preparation` |
| `time-management` | 番茄工作法 | `hermes skills install productivity/time-management` |

### 职业发展类

| Skill | 功能 | 安装命令 |
|-------|------|----------|
| `interview-preparation` | 面试准备 | `hermes skills install career/interview-preparation` |
| `github-repo-management` | GitHub仓库管理 | `hermes skills install github/github-repo-management` |

## Skills使用示例

### 1. 数据分析
```
帮我分析这个CSV文件的数据
```

### 2. 机器学习
```
用sklearn训练一个分类模型
```

### 3. Web开发
```
创建一个Flask Web应用
```

### 4. 算法练习
```
给我一个LeetCode题目的解法
```

### 5. 论文写作
```
帮我写一篇LaTeX论文
```

## Skills管理

### 查看已安装Skills
```bash
hermes skills list
```

### 查看Skill详情
```bash
hermes skills view <skill-name>
```

### 安装新Skill
```bash
hermes skills install <category>/<skill-name>
```

### 卸载Skill
```bash
hermes skills uninstall <skill-name>
```

## 自定义Skills

### 创建自己的Skill
```bash
hermes skills create my-skill
```

### Skill文件结构
```
my-skill/
├── SKILL.md          # Skill说明文档
├── references/       # 参考资料
├── templates/        # 模板文件
└── scripts/          # 辅助脚本
```

### Skill文档模板
```markdown
---
name: my-skill
description: "简短描述"
version: 1.0.0
author: YourName
---

# My Skill

## When to Use
- 使用场景1
- 使用场景2

## How to Run
1. 步骤1
2. 步骤2

## Quick Reference
- 常用命令
- 常用代码
```

## 最佳实践

1. **按需安装** - 只安装真正需要的Skills
2. **定期更新** - 保持Skills版本最新
3. **善用搜索** - `hermes skills search <keyword>`
4. **查看文档** - 使用前先看SKILL.md
5. **反馈问题** - 遇到bug及时反馈

## 常见问题

### Q: Skills安装失败？
A: 检查网络连接，或尝试手动安装

### Q: Skills使用报错？
A: 查看SKILL.md中的Prerequisites，安装依赖

### Q: 如何创建自己的Skills？
A: 参考 `hermes-agent-skill-authoring` Skill
