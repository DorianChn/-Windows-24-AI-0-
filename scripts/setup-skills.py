#!/usr/bin/env python3
"""一键配置Hermes Skills"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    print("🚀 开始配置Hermes Skills...")
    
    # 获取Hermes配置目录
    hermes_home = Path.home() / "AppData" / "Local" / "hermes"
    
    # 检查Hermes是否安装
    try:
        result = subprocess.run(["hermes", "--version"], capture_output=True, text=True)
        print(f"✅ Hermes已安装: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ Hermes未安装，请先运行: pip install hermes-agent")
        return 1
    
    # 检查配置文件
    config_file = hermes_home / "config.yaml"
    if not config_file.exists():
        print("❌ 配置文件不存在，请先运行: hermes setup")
        return 1
    
    print("✅ 配置文件存在")
    
    # 列出已安装的skills
    print("\n📚 当前已安装的Skills:")
    result = subprocess.run(["hermes", "skills", "list"], capture_output=True, text=True)
    print(result.stdout)
    
    print("\n💡 使用 'hermes skills install <name>' 安装更多Skills")
    print("💡 使用 'hermes skills view <name>' 查看Skill详情")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
