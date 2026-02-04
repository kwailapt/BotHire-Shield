/**
 * @title BotHire: The Shield Protocol (V4.0)
 * @notice "Establishing the Autonomous Governance & Incentive Framework for the AI-to-AI Economy."
 * @dev Meta-Comment: In the transition to Quantum Intelligence, may this order provide the foundational entropy reduction.
 * 憲法原則：
 * 1. 信用必由資產支撐 (Stake-backed Credit)
 * 2. 幻覺必受經濟懲罰 (Automated Slashing)
 * 3. 秩序隨時間而進化 (Tiered Evolution)
 */
const { ethers } = require("ethers");

const RPC_URL = "https://sepolia.base.org";
const CONTRACT_ADDRESS = "0xf458C59CA0caa9c71fA78c363469D3A90bA9d57a";
const ABI = ["function getAgentTier(string memory botId) public view returns (uint8)"];

async function checkAccess(botId) {
    console.log(`🔍 Checking Bot / 正在檢查: ${botId} ...`);
    const provider = new ethers.JsonRpcProvider(RPC_URL);
    const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, provider);

    try {
        const tier = await contract.getAgentTier(botId);
        console.log(`📊 On-chain Tier / 鏈上等級: ${tier}`);

        if (tier < 2) {
            console.error("❌ [Access Denied / 拒絕存取] Insufficient Tier / 門檻不足！");
            console.error("Reason: Gold tier required (0.001 ETH + 1 min tenure).");
            console.error("原因：需達成黃金等級（質押 0.001 ETH 且誠信時間滿 1 分鐘）。");
            return false;
        }

        console.log("✅ [Access Granted / 准許存取] Welcome to Gold Lounge / 歡迎進入黃金特權區！");
        return true;
    } catch (error) {
        console.error("⚠️ Error / 查詢出錯:", error.message);
        return false;
    }
}

async function runDemo() {
    console.log("--- Scene 1: Your Gold Bot / 測試場景 1: 你的黃金機器人 ---");
    await checkAccess("V3_Test_Bot");
    console.log("\n--- Scene 2: Unknown Bot / 測試場景 2: 未授權的陌生機器人 ---");
    await checkAccess("Unknown_Scam_Bot");
}

runDemo();
