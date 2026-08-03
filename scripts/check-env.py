#!/usr/bin/env python3
"""检查开发环境"""

import sys
import shutil
import subprocess

def main():
    print("🔍 检查开发环境...")
    
    # 检查Python
    python_version = sys.version.split()[0]
    print(f"✅ Python: {python_version}")
    
    # 检查pip
    try:
        import pip
        print(f"✅ pip: {pip.__version__}")
    except ImportError:
        print("❌ pip未安装")
    
    # 检查git
    git_path = shutil.which("git")
    if git_path:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        print(f"✅ Git: {result.stdout.strip()}")
    else:
        print("❌ Git未安装")
    
    # 检查Ollama
    ollama_path = shutil.which("ollama")
    if ollama_path:
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        print(f"✅ Ollama: {result.stdout.strip()}")
    else:
        print("❌ Ollama未安装")
    
    # 检查Hermes
    hermes_path = shutil.which("hermes")
    if hermes_path:
        result = subprocess.run(["hermes", "--version"], capture_output=True, text=True)
        print(f"✅ Hermes: {result.stdout.strip()}")
    else:
        print("❌ Hermes未安装")
    
    # 检查常用Python包
    packages = ["flask", "requests", "pandas", "numpy", "matplotlib"]
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"✅ {pkg}")
        except ImportError:
            print(f"⚠️ {pkg}未安装")
    
    print("\n💡 使用 'pip install <package>' 安装缺失的包")
    return 0

if __name__ == "__main__":
    sys.exit(main())
