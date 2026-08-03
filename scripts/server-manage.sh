#!/bin/bash
# server-manage.sh - Hermes服务器管理脚本
# 用法: bash server-manage.sh [命令]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 显示帮助
show_help() {
    echo -e "${BLUE}Hermes服务器管理工具${NC}"
    echo ""
    echo "用法: bash server-manage.sh [命令]"
    echo ""
    echo "命令:"
    echo "  status      查看服务状态"
    echo "  start       启动服务"
    echo "  stop        停止服务"
    echo "  restart     重启服务"
    echo "  logs        查看日志"
    echo "  update      更新Hermes"
    echo "  backup      备份配置"
    echo "  restore     恢复配置"
    echo "  health      健康检查"
    echo "  help        显示帮助"
}

# 查看状态
status() {
    echo -e "${BLUE}📋 Hermes服务状态:${NC}"
    systemctl status hermes
    echo ""
    echo -e "${BLUE}📊 资源使用:${NC}"
    echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')%"
    echo "内存: $(free -h | awk '/Mem:/ {print $3 "/" $2}')"
    echo "磁盘: $(df -h / | awk 'NR==2 {print $3 "/" $2 " (" $5 ")"}')"
}

# 启动服务
start() {
    echo -e "${BLUE}🚀 启动Hermes服务...${NC}"
    systemctl start hermes
    sleep 3
    if systemctl is-active --quiet hermes; then
        echo -e "${GREEN}✅ 服务已启动${NC}"
    else
        echo -e "${RED}❌ 服务启动失败${NC}"
        journalctl -u hermes --no-pager -n 20
    fi
}

# 停止服务
stop() {
    echo -e "${BLUE}🛑 停止Hermes服务...${NC}"
    systemctl stop hermes
    echo -e "${GREEN}✅ 服务已停止${NC}"
}

# 重启服务
restart() {
    echo -e "${BLUE}🔄 重启Hermes服务...${NC}"
    systemctl restart hermes
    sleep 3
    if systemctl is-active --quiet hermes; then
        echo -e "${GREEN}✅ 服务已重启${NC}"
    else
        echo -e "${RED}❌ 服务重启失败${NC}"
        journalctl -u hermes --no-pager -n 20
    fi
}

# 查看日志
logs() {
    echo -e "${BLUE}📜 Hermes日志:${NC}"
    journalctl -u hermes -f
}

# 更新Hermes
update() {
    echo -e "${BLUE}📦 更新Hermes...${NC}"
    
    # 停止服务
    systemctl stop hermes
    
    # 更新
    su - hermes -c "pip3 install --upgrade hermes-agent"
    
    # 启动服务
    systemctl start hermes
    sleep 3
    
    if systemctl is-active --quiet hermes; then
        echo -e "${GREEN}✅ 更新完成，服务已重启${NC}"
    else
        echo -e "${RED}❌ 更新后服务启动失败${NC}"
        journalctl -u hermes --no-pager -n 20
    fi
}

# 备份配置
backup() {
    echo -e "${BLUE}💾 备份Hermes配置...${NC}"
    /home/hermes/backup.sh
    echo -e "${GREEN}✅ 备份完成${NC}"
    echo "备份位置: /home/hermes/backups/"
}

# 恢复配置
restore() {
    echo -e "${BLUE}🔄 恢复Hermes配置...${NC}"
    
    # 列出备份
    backups=$(ls -t /home/hermes/backups/hermes-*.tar.gz 2>/dev/null | head -5)
    
    if [ -z "$backups" ]; then
        echo -e "${RED}❌ 没有找到备份文件${NC}"
        return 1
    fi
    
    echo "可用的备份:"
    echo "$backups" | nl
    
    read -p "选择备份 (输入数字): " choice
    backup_file=$(echo "$backups" | sed -n "${choice}p")
    
    if [ -z "$backup_file" ]; then
        echo -e "${RED}❌ 无效选择${NC}"
        return 1
    fi
    
    # 停止服务
    systemctl stop hermes
    
    # 恢复
    tar -xzf "$backup_file" -C /home/hermes/
    
    # 启动服务
    systemctl start hermes
    sleep 3
    
    if systemctl is-active --quiet hermes; then
        echo -e "${GREEN}✅ 恢复完成，服务已重启${NC}"
    else
        echo -e "${RED}❌ 恢复后服务启动失败${NC}"
        journalctl -u hermes --no-pager -n 20
    fi
}

# 健康检查
health() {
    echo -e "${BLUE}🏥 Hermes健康检查...${NC}"
    echo ""
    
    # 检查服务状态
    if systemctl is-active --quiet hermes; then
        echo -e "✅ 服务状态: ${GREEN}运行中${NC}"
    else
        echo -e "❌ 服务状态: ${RED}已停止${NC}"
    fi
    
    # 检查进程
    if pgrep -f "hermes gateway" > /dev/null; then
        echo -e "✅ 进程状态: ${GREEN}正常${NC}"
    else
        echo -e "❌ 进程状态: ${RED}异常${NC}"
    fi
    
    # 检查端口
    if netstat -tuln | grep -q ":8080"; then
        echo -e "✅ 端口状态: ${GREEN}监听中${NC}"
    else
        echo -e "⚠️ 端口状态: ${YELLOW}未监听${NC}"
    fi
    
    # 检查资源
    echo ""
    echo -e "${BLUE}📊 资源使用:${NC}"
    echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')%"
    echo "内存: $(free -h | awk '/Mem:/ {print $3 "/" $2}')"
    echo "磁盘: $(df -h / | awk 'NR==2 {print $3 "/" $2 " (" $5 ")"}')"
}

# 主函数
main() {
    case "${1:-help}" in
        status)
            status
            ;;
        start)
            start
            ;;
        stop)
            stop
            ;;
        restart)
            restart
            ;;
        logs)
            logs
            ;;
        update)
            update
            ;;
        backup)
            backup
            ;;
        restore)
            restore
            ;;
        health)
            health
            ;;
        help|*)
            show_help
            ;;
    esac
}

main "$@"
