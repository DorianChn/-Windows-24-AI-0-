"""
health-check.py — Hermes AI 系统健康检查
用法: python health-check.py
"""
import subprocess
import sys

def check_gateway():
    """检查 Gateway 进程是否在运行"""
    try:
        import psutil
        for proc in psutil.process_iter(['name', 'cmdline']):
            try:
                if proc.info['name'] == 'python.exe':
                    cmdline = ' '.join(proc.info['cmdline'] or [])
                    if 'gateway run' in cmdline:
                        return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return False
    except ImportError:
        # 没有 psutil，用 tasklist
        result = subprocess.run(
            ['tasklist', '/FI', 'IMAGENAME eq python.exe', '/FO', 'CSV'],
            capture_output=True, text=True
        )
        return 'gateway run' in result.stdout

def check_ollama():
    """检查 Ollama 服务是否可用"""
    try:
        result = subprocess.run(
            ['ollama', 'list'],
            capture_output=True, timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False

def check_gpu():
    """检查 GPU 是否可用"""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name', '--format=csv,noheader'],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0 and result.stdout.strip()
    except Exception:
        return False

def check_disk(min_gb=5):
    """检查磁盘剩余空间"""
    import shutil
    total, used, free = shutil.disk_usage("C:\\")
    free_gb = free / (1024 ** 3)
    return free_gb >= min_gb, f"{free_gb:.1f}GB free"

def main():
    checks = {
        'Gateway': check_gateway(),
        'Ollama': check_ollama(),
        'GPU': check_gpu(),
    }
    disk_ok, disk_info = check_disk()
    checks['Disk'] = disk_ok

    all_ok = all(checks.values())

    for service, ok in checks.items():
        icon = '✅' if ok else '❌'
        extra = f" ({disk_info})" if service == 'Disk' else ''
        print(f"  {icon} {service}{extra}")

    print()
    if all_ok:
        print("  所有服务正常")
    else:
        print("  ⚠️ 有服务异常，请检查")

    return 0 if all_ok else 1

if __name__ == '__main__':
    sys.exit(main())
