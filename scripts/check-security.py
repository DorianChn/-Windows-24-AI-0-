#!/usr/bin/env python3
"""安全检查"""

import subprocess
import sys
from pathlib import Path

def main():
    print("🔒 安全检查...")
    
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    
    # 检查敏感文件
    sensitive_patterns = [
        ".env",
        "*.key",
        "*.pem",
        "*.p12",
        "*.pfx",
        "*password*",
        "*secret*",
        "*token*",
        "*credential*",
    ]
    
    print("🔍 检查敏感文件...")
    found_sensitive = False
    for pattern in sensitive_patterns:
        for file in project_root.rglob(pattern):
            if ".git" not in str(file):
                print(f"  ⚠️ 发现敏感文件: {file.relative_to(project_root)}")
                found_sensitive = True
    
    if not found_sensitive:
        print("  ✅ 没有发现敏感文件")
    
    # 检查.gitignore
    gitignore = project_root / ".gitignore"
    if gitignore.exists():
        content = gitignore.read_text()
        required_patterns = [".env", "*.key", "*.pem", "__pycache__"]
        missing = [p for p in required_patterns if p not in content]
        
        if missing:
            print(f"\n⚠️ .gitignore缺少以下规则: {', '.join(missing)}")
        else:
            print("\n✅ .gitignore配置正确")
    else:
        print("\n⚠️ 没有找到.gitignore文件")
    
    # 检查依赖安全
    print("\n🔍 检查依赖安全...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--outdated"],
        capture_output=True,
        text=True
    )
    
    if result.stdout:
        print("  ⚠️ 发现过时的依赖:")
        print(result.stdout)
    else:
        print("  ✅ 所有依赖都是最新的")
    
    print("\n✅ 安全检查完成")
    return 0

if __name__ == "__main__":
    sys.exit(main())
