#!/usr/bin/env python3
"""格式化代码"""

import subprocess
import sys
from pathlib import Path

def main():
    print("🎨 格式化代码...")
    
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    
    # 查找Python文件
    py_files = list(project_root.rglob("*.py"))
    
    if not py_files:
        print("⚠️ 没有找到Python文件")
        return 0
    
    print(f"📋 找到 {len(py_files)} 个Python文件")
    
    # 使用black格式化
    print("\n🔧 使用black格式化...")
    result = subprocess.run(
        [sys.executable, "-m", "black", "."],
        cwd=project_root,
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("⚠️ black格式化失败")
        print(result.stderr)
    else:
        print("✅ black格式化完成")
    
    # 使用flake8检查
    print("\n🔍 使用flake8检查...")
    result = subprocess.run(
        [sys.executable, "-m", "flake8", "--max-line-length=100", "."],
        cwd=project_root,
        capture_output=True,
        text=True
    )
    
    if result.stdout:
        print("⚠️ 发现以下问题:")
        print(result.stdout)
    else:
        print("✅ 没有发现问题")
    
    print("\n✅ 代码格式化完成")
    return 0

if __name__ == "__main__":
    sys.exit(main())
