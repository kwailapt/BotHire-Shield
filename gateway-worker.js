/**
 * 🛡️ BotHire: The Shield Protocol Gateway (V4.0)
 * [Edge Sentinel / 邊緣哨兵]
 */

const RPC_URL = "https://sepolia.base.org";
const CONTRACT_ADDRESS = "0xf458C59CA0caa9c71fA78c363469D3A90bA9d57a";
const ABI_FRAGMENT = [{"inputs":[{"internalType":"string","name":"botId","type":"string"}],"name":"getAgentTier","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"}];

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const botId = url.searchParams.get("botId");

    if (!botId) {
      return new Response(JSON.stringify({ error: "Missing botId / 缺少 BotID" }), {
        status: 400,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }

    try {
      // 這裡模擬對 Base Sepolia 的鏈上 RPC 調用
      // 在 Workers 環境中，我們會使用標準 fetch 封裝 RPC
      const tier = await queryOnChainTier(botId);

      return new Response(JSON.stringify({
        protocol: "The Shield Protocol",
        version: "4.0",
        botId: botId,
        tier: tier,
        access: tier >= 2 ? "GRANTED" : "DENIED",
        timestamp: Date.now()
      }), {
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), { status: 500 });
    }
  }
};

async function queryOnChainTier(botId) {
  // 此處為 RPC 查詢邏輯（簡化版）
  // 實際上會發送 POST 到 RPC_URL
  return 2; // 測試期間預設返回 Gold
}
