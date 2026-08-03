#!/usr/bin/env python3
"""备份Hermes配置"""

import shutil
import sys
from datetime import datetime
from pathlib import Path

def main():
    print("💾 开始备份Hermes配置...")
    
    hermes_home = Path.home() / "AppData" / "Local" / "hermes"
    backup_dir = Path.home() / "Documents" / "HermesBackups"
    
    # 创建备份目录
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成备份文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"hermes_config_{timestamp}.zip"
    
    # 备份配置文件
    config_file = hermes_home / "config.yaml"
    env_file = hermes_home / ".env"
    skills_dir = hermes_home / "skills"
    
    if not config_file.exists():
        print("❌ 配置文件不存在")
        return 1
    
    # 创建zip文件
    import zipfile
    with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 备份配置文件
        zipf.write(config_file, "config.yaml")
        
        # 备份环境变量
        if env_file.exists():
            zipf.write(env_file, ".env")
        
        # 备份skills目录
        if skills_dir.exists():
            for file in skills_dir.rglob("*.md"):
                zipf.write(file, f"skills/{file.relative_to(skills_dir)}")
    
    print(f"✅ 备份完成: {backup_file}")
    print(f"📦 文件大小: {backup_file.stat().st_size / 1024:.1f} KB")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
