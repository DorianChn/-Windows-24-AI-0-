#!/usr/bin/env python3
"""列出所有可用的Hermes Skills"""

import subprocess
import sys

def main():
    print("📚 列出所有可用的Hermes Skills...")
    
    # 列出已安装的skills
    print("\n✅ 已安装的Skills:")
    result = subprocess.run(["hermes", "skills", "list"], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("❌ 获取skills列表失败")
    
    # 列出可用的skills
    print("\n📦 可安装的Skills:")
    result = subprocess.run(["hermes", "skills", "list", "--available"], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("❌ 获取可用skills列表失败")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
