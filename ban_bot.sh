#!/bin/bash
# 用法: ./ban_bot.sh [BotID] [原因]

BOT_ID=$1
REASON=$2

if [ -z "$BOT_ID" ]; then
    echo "錯誤: 缺少 Bot ID"
    exit 1
fi

echo "🛡️ BotHire-Shield: 正在全球封鎖 Bot [$BOT_ID]..."
wrangler kv key put --binding=SHIELD_KV "$BOT_ID" "$REASON" --remote
