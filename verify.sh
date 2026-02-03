#!/bin/bash

# 1. 檢查依賴工具
if ! command -v ajv &> /dev/null; then
    echo "安裝校驗工具 ajv-cli..."
    npm install -g ajv-cli
fi

# 2. 執行 Schema 校驗
echo "🔍 正在校驗 aSLA 協議格式..."
ajv validate -s schemas/aSLA_schema.json -d schemas/sample_aSLA.json

if [ $? -eq 0 ]; then
    echo "✅ 協議符合 x402 標準！"
    exit 0
else
    echo "❌ 協議格式錯誤！"
    exit 1
fi
