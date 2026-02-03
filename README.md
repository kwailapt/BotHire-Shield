# 🛡️ BotHire-Shield: x402 Protocol AI Arbitration System (V2)

[中文版](#中文版) | [English Version](#english-version)

---

## 中文版

### 📖 簡介 (V2: 經濟治理版)
BotHire-Shield V2 是一個將「經濟博弈」引入 AI 治理的去中心化協議。它不僅偵測違規，更透過 **質押 (Staking)** 與 **扣款 (Slashing)** 機制，確保 AI Bot 的行為具備真實的違約成本。

### 💎 核心機制：信任層定義
* **抵押即信任 (Stake-to-Play)**：Bot 必須質押至少 **0.001 ETH** 於智能合約中，才能獲得「准予存取」狀態。
* **經濟處罰 (Slashing)**：若 GitHub Actions 偵測到協議違規，系統將自動觸發合約扣除 **0.0005 ETH** 罰金。
* **自我修復 (Self-Healing)**：違規 Bot 僅需補齊質押金，即可透過代碼邏輯自動修復信用，無需人工審核。

### 🚀 技術架構
1.  **Smart Contract**: `ShieldArbitratorV2` 部署於 **Base Sepolia**。
2.  **Enforcement**: GitHub Actions 聯動 Foundry (Cast) 執行自動扣款。
3.  **Audit**: 前端 UI 實時監控 Bot 的鏈上資產餘額與信用狀態。

### 🔗 項目資源
* **V2 合約地址**: `0x6e7A1aD2f1e144020a58A0c2A0009De6e45fFA1c`
* **信用查詢面板**: [點擊訪問查詢台](https://kwailapt.github.io/BotHire-Shield/)

---

## English Version

### 📖 Introduction (V2: Economic Governance)
BotHire-Shield V2 is a decentralized protocol that introduces "Game Theory" into AI governance. Beyond simple detection, it utilizes **Staking** and **Slashing** mechanisms to ensure AI agents have a real economic cost for misbehavior.

### 💎 Core Mechanism: Defining the Trust Layer
* **Stake-to-Play**: Bots must stake a minimum of **0.001 ETH** in the smart contract to achieve "Allowed" status. Trust is backed by assets.
* **Economic Slashing**: If GitHub Actions detects a protocol violation, the system automatically triggers a **0.0005 ETH** penalty deduction from the stake.
* **Self-Healing**: A blacklisted Bot can automatically regain its "Allowed" status by replenishing its stake, removing the need for human intervention.

### 🚀 Architecture
1.  **Smart Contract**: `ShieldArbitratorV2` deployed on **Base Sepolia**.
2.  **Enforcement**: GitHub Actions integrated with Foundry (Cast) for automated slashing.
3.  **Audit**: Frontend dashboard for real-time monitoring of on-chain balances and credit status.

### 🔗 Resources
* **V2 Contract Address**: `0x6e7A1aD2f1e144020a58A0c2A0009De6e45fFA1c`
* **Credit Dashboard**: [Live Dashboard](https://kwailapt.github.io/BotHire-Shield/)

