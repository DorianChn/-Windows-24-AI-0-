#!/usr/bin/env python3
"""更新项目文档"""

import os
import sys
from pathlib import Path

def main():
    print("📝 更新项目文档...")
    
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs"
    
    # 列出所有文档
    docs = list(docs_dir.glob("*.md"))
    print(f"📚 找到 {len(docs)} 个文档:")
    
    for doc in sorted(docs):
        size = doc.stat().st_size / 1024
        print(f"  📄 {doc.name} ({size:.1f} KB)")
    
    # 检查README
    readme = project_root / "README.md"
    if readme.exists():
        print(f"\n📖 README.md ({readme.stat().st_size / 1024:.1f} KB)")
    
    # 生成目录
    toc = []
    for doc in sorted(docs):
        name = doc.stem
        title = name.split("-", 1)[-1] if "-" in name else name
        toc.append(f"- [{title}](docs/{doc.name})")
    
    print("\n📋 文档目录:")
    print("\n".join(toc))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
