#!/usr/bin/env python3
"""快速提交代码到GitHub"""

import subprocess
import sys
from datetime import datetime

def main():
    print("📦 快速提交代码...")
    
    # 检查是否在git仓库
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ 当前目录不是git仓库")
        return 1
    
    # 获取当前状态
    status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    if not status.stdout.strip():
        print("✅ 没有需要提交的更改")
        return 0
    
    print("📋 当前更改:")
    print(status.stdout)
    
    # 添加所有文件
    subprocess.run(["git", "add", "."])
    
    # 生成提交信息
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_msg = f"更新: {timestamp}"
    
    # 提交
    result = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ 提交失败")
        print(result.stderr)
        return 1
    
    print(f"✅ 提交成功: {commit_msg}")
    
    # 推送到远程
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    if result.returncode != 0:
        print("⚠️ 推送失败，可能需要先拉取远程更改")
        print(result.stderr)
        return 1
    
    print("✅ 推送成功")
    return 0

if __name__ == "__main__":
    sys.exit(main())
