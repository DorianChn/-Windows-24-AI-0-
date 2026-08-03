#!/usr/bin/env python3
"""运行测试"""

import subprocess
import sys
from pathlib import Path

def main():
    print("🧪 运行测试...")
    
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    
    # 查找测试文件
    test_files = list(project_root.rglob("test_*.py"))
    
    if not test_files:
        print("⚠️ 没有找到测试文件")
        return 0
    
    print(f"📋 找到 {len(test_files)} 个测试文件:")
    for file in test_files:
        print(f"  - {file.relative_to(project_root)}")
    
    # 运行pytest
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v"],
        cwd=project_root,
        capture_output=True,
        text=True
    )
    
    print("\n📊 测试结果:")
    print(result.stdout)
    
    if result.returncode != 0:
        print("❌ 测试失败")
        print(result.stderr)
        return 1
    
    print("✅ 所有测试通过")
    return 0

if __name__ == "__main__":
    sys.exit(main())
