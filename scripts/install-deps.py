#!/usr/bin/env python3
"""安装项目依赖"""

import subprocess
import sys

def main():
    print("📦 安装项目依赖...")
    
    # 基础依赖
    base_packages = [
        "requests",
        "beautifulsoup4",
        "flask",
        "fastapi",
        "uvicorn",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "pytest",
        "black",
        "flake8",
        "mypy",
    ]
    
    # 安装依赖
    for package in base_packages:
        print(f"安装 {package}...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"⚠️ 安装 {package} 失败")
            print(result.stderr)
        else:
            print(f"✅ {package} 安装成功")
    
    print("\n✅ 所有依赖安装完成")
    return 0

if __name__ == "__main__":
    sys.exit(main())
