#!/bin/bash
# server-setup.sh - Hermes服务器一键部署脚本
# 用法: bash server-setup.sh

set -e

echo "🚀 开始部署Hermes到服务器..."
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查是否为root用户
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}❌ 请使用root用户运行此脚本${NC}"
    echo "用法: sudo bash server-setup.sh"
    exit 1
fi

# 获取配置
read -p "请输入服务器密码 (用于hermes用户): " HERMES_PASSWORD
read -p "请输入阿里云百炼API Key: " DASHSCOPE_API_KEY

if [ -z "$DASHSCOPE_API_KEY" ]; then
    echo -e "${RED}❌ API Key不能为空${NC}"
    exit 1
fi

echo ""
echo "📦 安装系统依赖..."

# 更新系统
apt update
apt upgrade -y

# 安装依赖
apt install -y python3 python3-pip python3-venv git curl wget htop

echo -e "${GREEN}✅ 系统依赖安装完成${NC}"

echo ""
echo "👤 创建hermes用户..."

# 创建用户
if id "hermes" &>/dev/null; then
    echo "用户hermes已存在"
else
    useradd -m -s /bin/bash hermes
    echo "hermes:$HERMES_PASSWORD" | chpasswd
    echo -e "${GREEN}✅ 用户创建完成${NC}"
fi

echo ""
echo "⚙️ 配置Hermes..."

# 切换到hermes用户并配置
su - hermes << EOF

# 安装Hermes
pip3 install --user hermes-agent

# 创建配置目录
mkdir -p ~/.hermes

# 配置环境变量
cat > ~/.hermes/.env << 'ENVEOF'
# 阿里云百炼
DASHSCOPE_API_KEY=$DASHSCOPE_API_KEY

# 其他配置（可选）
# TELEGRAM_BOT_TOKEN=
# DISCORD_TOKEN=
ENVEOF

# 配置Hermes
cat > ~/.hermes/config.yaml << 'CONFIGEOF'
model:
  default: deepseek-v4-flash
  provider: alibaba
  context_length: 65536
  aliases:
    deep: deepseek/deepseek-v4-flash

providers:
  alibaba:
    base_url: https://ws-d2zlnzz8btbed5od.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
    request_timeout_seconds: 120
    stale_timeout_seconds: 90

compression:
  summary_model: deepseek-v4-flash
  enabled: true
  threshold: 0.5
  target_ratio: 0.2

auxiliary:
  compression:
    model: deepseek-v4-flash
    provider: alibaba

terminal:
  backend: local
  timeout: 180

display:
  language: zh
  streaming: true
  tool_progress: all

memory:
  memory_enabled: true
  user_profile_enabled: true

skills:
  platform_disabled:
    cron: []
CONFIGEOF

echo "✅ Hermes配置完成"

EOF

echo -e "${GREEN}✅ Hermes安装配置完成${NC}"

echo ""
echo "🔧 配置系统服务..."

# 配置systemd服务
cat > /etc/systemd/system/hermes.service << 'SERVICEEOF'
[Unit]
Description=Hermes AI Agent
After=network.target

[Service]
Type=simple
User=hermes
WorkingDirectory=/home/hermes
ExecStart=/home/hermes/.local/bin/hermes gateway run
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
SERVICEEOF

# 启用服务
systemctl daemon-reload
systemctl enable hermes

echo -e "${GREEN}✅ 系统服务配置完成${NC}"

echo ""
echo "🛡️ 配置防火墙..."

# 配置防火墙
if command -v ufw &> /dev/null; then
    ufw allow ssh
    ufw allow 80/tcp
    ufw allow 443/tcp
    ufw --force enable
    echo -e "${GREEN}✅ 防火墙配置完成${NC}"
else
    echo -e "${YELLOW}⚠️ ufw未安装，请手动配置防火墙${NC}"
fi

echo ""
echo "🚀 启动Hermes服务..."

# 启动服务
systemctl start hermes

# 等待服务启动
sleep 5

# 检查服务状态
if systemctl is-active --quiet hermes; then
    echo -e "${GREEN}✅ Hermes服务已启动${NC}"
else
    echo -e "${RED}❌ Hermes服务启动失败${NC}"
    echo "查看日志: journalctl -u hermes -f"
    exit 1
fi

echo ""
echo "📋 配置备份定时任务..."

# 配置备份cron
cat > /home/hermes/backup.sh << 'BACKUPEOF'
#!/bin/bash
# 备份Hermes配置

BACKUP_DIR="/home/hermes/backups"
mkdir -p $BACKUP_DIR

DATE=$(date +%Y%m%d_%H%M%S)
tar -czf $BACKUP_DIR/hermes-$DATE.tar.gz ~/.hermes/

# 保留最近7天的备份
find $BACKUP_DIR -name "hermes-*.tar.gz" -mtime +7 -delete
BACKUPEOF

chmod +x /home/hermes/backup.sh
chown hermes:hermes /home/hermes/backup.sh

# 添加cron任务
su - hermes << 'EOF'
(crontab -l 2>/dev/null; echo "0 2 * * * /home/hermes/backup.sh") | crontab -
EOF

echo -e "${GREEN}✅ 备份定时任务配置完成${NC}"

echo ""
echo "=========================================="
echo -e "${GREEN}🎉 Hermes部署完成！${NC}"
echo "=========================================="
echo ""
echo "📋 常用命令:"
echo "  查看状态: systemctl status hermes"
echo "  查看日志: journalctl -u hermes -f"
echo "  重启服务: systemctl restart hermes"
echo "  停止服务: systemctl stop hermes"
echo "  编辑配置: vim /home/hermes/.hermes/config.yaml"
echo "  备份配置: /home/hermes/backup.sh"
echo ""
echo "📋 下一步:"
echo "  1. 配置微信Bot (参考docs/04-微信bot部署.md)"
echo "  2. 配置Skills (hermes skills list)"
echo "  3. 配置定时任务 (hermes cron list)"
echo ""
echo "📋 访问地址:"
echo "  本地: http://localhost:8080"
echo "  远程: http://$(curl -s ifconfig.me)"
echo ""
echo -e "${GREEN}✅ 祝你使用愉快！${NC}"
