#!/usr/bin/env python3
"""清理项目文件"""

import os
import sys
import shutil
from pathlib import Path

def main():
    print("🧹 清理项目文件...")
    
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    
    # 要清理的目录和文件
    clean_targets = [
        "__pycache__",
        "*.pyc",
        "*.pyo",
        ".pytest_cache",
        ".coverage",
        "htmlcov",
        "*.egg-info",
        "dist",
        "build",
        ".eggs",
        "*.egg",
        ".mypy_cache",
        ".tox",
        ".nox",
        "*.log",
        "*.tmp",
        "*.bak",
        "*.swp",
        "*.swo",
        "*~",
        ".DS_Store",
        "Thumbs.db",
        "desktop.ini",
    ]
    
    cleaned = 0
    
    for target in clean_targets:
        if "*" in target:
            # 使用glob匹配
            for file in project_root.rglob(target):
                if ".git" not in str(file):
                    try:
                        if file.is_file():
                            file.unlink()
                        elif file.is_dir():
                            shutil.rmtree(file)
                        print(f"  删除: {file.relative_to(project_root)}")
                        cleaned += 1
                    except Exception as e:
                        print(f"  ⚠️ 无法删除 {file.relative_to(project_root)}: {e}")
        else:
            # 直接删除目录
            for dir in project_root.rglob(target):
                if ".git" not in str(dir) and dir.is_dir():
                    try:
                        shutil.rmtree(dir)
                        print(f"  删除目录: {dir.relative_to(project_root)}")
                        cleaned += 1
                    except Exception as e:
                        print(f"  ⚠️ 无法删除 {dir.relative_to(project_root)}: {e}")
    
    print(f"\n✅ 清理完成，共删除 {cleaned} 个文件/目录")
    return 0

if __name__ == "__main__":
    sys.exit(main())
