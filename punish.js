/**
 * @title BotHire: The Shield Protocol (V4.0) - The Executioner
 * @notice "Automated Slashing Module: Code is Law, and Law has a Price."
 */
const { ethers } = require("ethers");
require('dotenv').config();

const RPC_URL = process.env.RPC_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const CONTRACT_ADDRESS = "0xf458C59CA0caa9c71fA78c363469D3A90bA9d57a";

const ABI = [
    "function slashAgent(string memory botId) public",
    "function getAgentTier(string memory botId) public view returns (uint8)"
];

async function executePunishment(botId) {
    const provider = new ethers.JsonRpcProvider(RPC_URL);
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
    const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, wallet);

    console.log(`🧨 [Alert / 警告] Malicious activity detected! Slashing Bot: ${botId}...`);

    try {
        const tx = await contract.slashAgent(botId);
        console.log(`📡 [Transaction Sent / 交易發送]: ${tx.hash}`);
        await tx.wait();
        console.log(`✅ [Success / 成功] Penalty executed! Bot blacklisted.`);

        const newTier = await contract.getAgentTier(botId);
        console.log(`📉 [New Status / 當前狀態]: Tier ${newTier}`);
    } catch (error) {
        console.error("❌ [Failed / 失敗]:", error.reason || error.message);
    }
}

executePunishment("V3_Test_Bot");
