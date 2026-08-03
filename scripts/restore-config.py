#!/usr/bin/env python3
"""恢复Hermes配置"""

import shutil
import sys
import zipfile
from pathlib import Path

def main():
    print("🔄 开始恢复Hermes配置...")
    
    hermes_home = Path.home() / "AppData" / "Local" / "hermes"
    backup_dir = Path.home() / "Documents" / "HermesBackups"
    
    # 列出备份文件
    backups = list(backup_dir.glob("hermes_config_*.zip"))
    if not backups:
        print("❌ 没有找到备份文件")
        return 1
    
    # 按时间排序
    backups.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    print("📋 可用的备份:")
    for i, backup in enumerate(backups[:10], 1):
        size = backup.stat().st_size / 1024
        print(f"  {i}. {backup.name} ({size:.1f} KB)")
    
    # 选择备份
    try:
        choice = int(input("\n选择备份 (输入数字): ")) - 1
        if choice < 0 or choice >= len(backups):
            raise ValueError
    except (ValueError, EOFError):
        print("❌ 无效选择")
        return 1
    
    backup_file = backups[choice]
    print(f"\n📦 恢复备份: {backup_file.name}")
    
    # 解压备份
    with zipfile.ZipFile(backup_file, 'r') as zipf:
        zipf.extractall(hermes_home)
    
    print("✅ 恢复完成")
    print("💡 重启Hermes使配置生效: hermes gateway restart")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
