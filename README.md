# 🛡️ BotHire-Shield: x402 Protocol AI Arbitration System

[中文版](#中文版) | [English Version](#english-version)

---

## 中文版

### 📖 簡介
BotHire-Shield 是一個全自動化、去中心化的 AI 服務安全防線。它結合了 **GitHub Actions** 的自動化工作流與 **Base 區塊鏈** 的不可篡改性，為 $x402$ 協議提供鏈上執法保障。當 AI Bot 提交的協議不符合標準時，系統會自動將其標記並記錄在區塊鏈黑名單中。

### 🚀 系統核心流程
1.  **協議提交 (Submit)**：AI 代理或開發者推送 `aSLA` (AI Service Level Agreement) 協議 JSON 文件。
2.  **自動校驗 (Validate)**：GitHub Actions 透過 `ajv-cli` 根據嚴格的 JSON Schema 進行即時校驗。
3.  **鏈上執法 (Enforce)**：
    * **校驗成功**：Bot 被視為信用良好，系統不採取行動。
    * **校驗失敗**：Actions 自動調用部署在 **Base Sepolia** 上的智能合約，將該 Bot ID 永久標記為「違規」。
4.  **信用公示 (Audit)**：透過前端面板，全球用戶可即時查詢任何 Bot 的鏈上信用狀態。

### 🛠️ 技術棧
* **Smart Contract**: Solidity (Deployed on Base Sepolia)
* **Security Framework**: Foundry (Forge & Cast)
* **Automation**: GitHub Actions
* **Verification**: JSON Schema (ajv)
* **Frontend**: Ethers.js & GitHub Pages

### 🔗 項目資源
* **智能合約地址**: `0xa7D1299B45294e4F34fD0cF0da4100d78Df26090`
* **信用查詢面板**: [點擊訪問查詢台](https://kwailapt.github.io/BotHire-Shield/)
* **區塊鏈瀏覽器**: [在 BaseScan 查看合約](https://sepolia.basescan.org/address/0xa7D1299B45294e4F34fD0cF0da4100d78Df26090)

---

## English Version

### 📖 Introduction
BotHire-Shield is a fully automated, decentralized security layer for AI agents. It integrates **GitHub Actions** workflows with the immutability of the **Base Blockchain** to provide on-chain enforcement for the $x402$ protocol. It ensures that any AI agent failing to meet agreed-upon standards is held accountable on-chain.

### 🚀 System Architecture
1.  **Submit**: AI agents or developers push an `aSLA` (AI Service Level Agreement) JSON file.
2.  **Validate**: GitHub Actions performs real-time validation via `ajv-cli` against a strict JSON Schema.
3.  **Enforce**: 
    * **Pass**: The Bot is maintained as "Trusted".
    * **Fail**: Actions automatically triggers a transaction to the smart contract on **Base Sepolia**, blacklisting the Bot ID permanently.
4.  **Audit**: A public frontend dashboard allows anyone to query a Bot's on-chain credit status instantly.

### 🛠️ Tech Stack
* **Smart Contract**: Solidity (Deployed on Base Sepolia)
* **Security Framework**: Foundry (Forge & Cast)
* **Automation**: GitHub Actions
* **Verification**: JSON Schema (ajv)
* **Frontend**: Ethers.js & GitHub Pages

### 🔗 Resources
* **Contract Address**: `0xa7D1299B45294e4F34fD0cF0da4100d78Df26090`
* **Credit Dashboard**: [Visit Live Dashboard](https://kwailapt.github.io/BotHire-Shield/)
* **Explorer**: [View on BaseScan](https://sepolia.basescan.org/address/0xa7D1299B45294e4F34fD0cF0da4100d78Df26090)

