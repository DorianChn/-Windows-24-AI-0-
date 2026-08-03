#!/usr/bin/env python3
"""生成项目报告"""

import os
import sys
from pathlib import Path
from datetime import datetime

def main():
    print("📊 生成项目报告...")
    
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    
    # 统计文件
    stats = {
        "python": 0,
        "markdown": 0,
        "javascript": 0,
        "html": 0,
        "css": 0,
        "other": 0
    }
    
    for file in project_root.rglob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if ext == ".py":
                stats["python"] += 1
            elif ext == ".md":
                stats["markdown"] += 1
            elif ext == ".js":
                stats["javascript"] += 1
            elif ext == ".html":
                stats["html"] += 1
            elif ext == ".css":
                stats["css"] += 1
            else:
                stats["other"] += 1
    
    # 生成报告
    report = f"""# 项目报告

生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 文件统计

| 类型 | 数量 |
|------|------|
| Python | {stats['python']} |
| Markdown | {stats['markdown']} |
| JavaScript | {stats['javascript']} |
| HTML | {stats['html']} |
| CSS | {stats['css']} |
| 其他 | {stats['other']} |
| **总计** | **{sum(stats.values())}** |

## 项目结构

"""
    
    # 添加目录结构
    for item in sorted(project_root.rglob("*")):
        if item.is_file() and ".git" not in str(item):
            rel_path = item.relative_to(project_root)
            report += f"- {rel_path}\n"
    
    # 保存报告
    report_file = project_root / "docs" / "PROJECT_REPORT.md"
    report_file.write_text(report, encoding="utf-8")
    
    print(f"✅ 报告生成完成: {report_file}")
    print(f"📁 文件统计:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  总计: {sum(stats.values())}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
