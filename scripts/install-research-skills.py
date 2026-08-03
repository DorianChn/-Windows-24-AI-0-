#!/usr/bin/env python3
"""安装学术研究Skills"""

import subprocess
import sys
from pathlib import Path

def main():
    print("📚 安装学术研究Skills...")
    
    # 学术研究skills列表
    research_skills = [
        "literature-review",
        "paper-novelty-design",
        "arxiv-digest",
        "scientific-figure",
        "citation-management",
        "research-proposal",
        "paper-writing",
    ]
    
    # 检查Hermes是否安装
    try:
        result = subprocess.run(["hermes", "--version"], capture_output=True, text=True)
        print(f"✅ Hermes已安装: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ Hermes未安装，请先运行: pip install hermes-agent")
        return 1
    
    # 列出已安装的skills
    print("\n📋 当前已安装的Skills:")
    result = subprocess.run(["hermes", "skills", "list"], capture_output=True, text=True)
    print(result.stdout)
    
    # 检查学术研究skills
    print("\n🔍 检查学术研究Skills:")
    installed_skills = result.stdout
    
    for skill in research_skills:
        if skill in installed_skills:
            print(f"  ✅ {skill} - 已安装")
        else:
            print(f"  ⚠️ {skill} - 未安装")
    
    print("\n💡 使用 'hermes skills view <skill-name>' 查看skill详情")
    print("💡 使用 'hermes skills install <skill-name>' 安装skill")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
