#!/usr/bin/env python3
"""部署到GitHub Pages"""

import subprocess
import sys
from pathlib import Path

def main():
    print("🚀 部署到GitHub Pages...")
    
    # 检查是否在git仓库
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ 当前目录不是git仓库")
        return 1
    
    # 获取远程仓库信息
    result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
    if "github.com" not in result.stdout:
        print("❌ 远程仓库不是GitHub")
        return 1
    
    # 提交所有更改
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update for GitHub Pages"])
    
    # 推送到main分支
    result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ 推送失败")
        print(result.stderr)
        return 1
    
    print("✅ 推送成功")
    print("\n📋 接下来需要:")
    print("1. 在GitHub仓库设置中启用GitHub Pages")
    print("2. 选择分支: main")
    print("3. 选择目录: / (root) 或 /docs")
    print("4. 保存设置")
    print("5. 等待几分钟，访问 https://your-username.github.io/repo-name")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
