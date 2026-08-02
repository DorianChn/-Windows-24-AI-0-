# 04 微信 Bot 部署

> 让 AI 助手 24 小时在微信上在线

## 1. 原理

```
微信 ←→ iLink Bot（微信协议桥）←→ Hermes Gateway ←→ AI Agent（本地模型）
```

iLink 是一个微信机器人框架，提供微信消息的收发接口。Hermes Gateway 连接 iLink，实现微信消息自动回复。

## 2. 安装 iLink Bot

参考 iLink 官方文档配置微信登录，获取 bot ID。

## 3. 配置 Hermes Gateway

在 `~/.hermes/config.yaml` 中：

```yaml
gateway:
  enabled: true
  platforms:
    weixin:
      enabled: true
      bot_id: "你的iLink bot ID"    # 格式如 xxx@im.bot
      user_id: "你的微信用户ID"      # 格式如 xxx@im.wechat
```

## 4. 启动 Gateway

```bash
# 前台启动（调试用）
hermes gateway run

# 后台启动（生产用）
hermes gateway run &
```

## 5. 限制 Gateway 工具集

微信端不需要所有工具，精简可省 token：

```yaml
# config.yaml
platform_toolsets:
  weixin:
    enabled:
      - terminal
      - web
      - file
      - memory
      - todo
      # 只开需要的，不要全开
```

## 6. 防双实例

**重要教训：** iLink 单账号只允许一个长连接。同时跑两个 gateway 会导致：

- 30 秒 rate limit 频发
- send failed
- gateway 反复崩溃退出
- 消息无回复

检查是否双实例：

```powershell
Get-CimInstance Win32_Process | Where-Object {$_.Name -eq 'python.exe' -and $_.CommandLine -match 'gateway run'}
```

## 7. 云端模型配置（推荐）

本地模型推理时，gateway 会阻塞等待。建议用云端模型做压缩/辅助：

```yaml
# config.yaml
auxiliary:
  compression:
    provider: alibaba
    model: deepseek-v4-flash
```

## 常见问题

**Q: 微信收不到回复？**
A: 检查 gateway 是否在运行（`hermes gateway status`），检查 iLink 是否在线。

**Q: 消息延迟很大？**
A: 本地模型推理需要时间，qwen3:64k 约 20-30 token/s。简单问题几秒，复杂问题可能 30 秒+。

**Q: 怎么确认只有一个 gateway 实例？**
A: 用上面的 PowerShell 命令检查，只应该有一个进程。
