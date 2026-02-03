# BotHire-Shield: AI Agent Governance Protocol (V3.1)

[English] | [中文]

## 📝 Overview / 概述
A decentralized AI credit protocol built on Base Sepolia, implementing tiered access control via on-chain staking and time-weighted loyalty.
基於 Base Sepolia 構建的去中心化 AI 信用協議，透過鏈上質押與時間加權機制實現分層權限控管。

## 🚀 Key Milestones / 今日里程碑
- **Tiered Logic / 信用分層**: Implemented Assets + Time dual verification. (資產 + 時間雙重驗證)
- **Gatekeeper / 守門人**: Node.js script for real-time Tier-based interception. (實時等級攔截腳本)
- **Slashing / 自動懲罰**: Automated penalty system to reset malicious bots to Tier 0. (自動化懲罰與等級歸零機制)

## 🛠️ Technical Specs / 技術規格
- **Contract Address / 合約地址**: `0xf458C59CA0caa9c71fA78c363469D3A90bA9d57a`
- **Tiers / 等級定義**:
  - **Tier 0 (Bronze)**: Initial / Blacklisted (初始狀態 / 黑名單)
  - **Tier 1 (Silver)**: Stake > 0.0005 ETH (基礎誠信)
  - **Tier 2 (Gold)**: Stake > 0.001 ETH + 1 min tenure (黃金特權)

## 🧪 Test Results / 測試報告
1. **Staking / 質押**: 0.0015 ETH -> Verified.
2. **Promotion / 晉升**: 0s (Tier 1) -> 60s (Tier 2) -> Verified.
3. **Slashing / 懲罰**: Executed -> Tier reset to 0 (Blacklisted) -> Verified.

## 📦 Usage / 使用方法
```bash
# Check Access / 權限檢查
node gatekeeper.js

# Execute Penalty / 執行懲罰
node punish.js


---

### 2. 雙語化腳本註解 (`gatekeeper.js`)
讓我們把腳本內的輸出也改為雙語，這能讓你的後端日誌更專業：

```bash
cat <<'EOF' > gatekeeper.js
const { ethers } = require("ethers");

const RPC_URL = "https://sepolia.base.org";
const CONTRACT_ADDRESS = "0xf458C59CA0caa9c71fA78c363469D3A90bA9d57a";
const ABI = ["function getAgentTier(string memory botId) public view returns (uint8)"];

async function checkAccess(botId) {
    console.log(`🔍 Checking Bot: ${botId} ...`);
    const provider = new ethers.JsonRpcProvider(RPC_URL);
    const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, provider);

    try {
        const tier = await contract.getAgentTier(botId);
        console.log(`📊 On-chain Tier / 鏈上等級: ${tier}`);

        if (tier < 2) {
            console.error("❌ [Access Denied / 拒絕存取] Insufficient Tier!");
            console.error("Reason: Gold tier required (0.001 ETH + 1 min tenure).");
            return false;
        }

        console.log("✅ [Access Granted / 准許存取] Welcome to Gold Lounge!");
        return true;
    } catch (error) {
        console.error("⚠️ Error / 查詢出錯:", error.message);
        return false;
    }
}

async function runDemo() {
    console.log("--- Scene 1: Your Gold Bot / 測試黃金機器人 ---");
    await checkAccess("V3_Test_Bot");
    console.log("\n--- Scene 2: Unknown Bot / 測試未知機器人 ---");
    await checkAccess("Unknown_Scam_Bot");
}

runDemo();
