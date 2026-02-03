export default {
  async fetch(request, env) {
    const x402Token = request.headers.get("X-402-Shield-Token");

    // 1. 協議標頭檢查 (第一道關卡)
    if (!x402Token) {
      return new Response(JSON.stringify({
        error: "Protocol Violation",
        message: "X-402-Shield-Token required for BotHire-Shield access."
      }), { 
        status: 402, 
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } 
      });
    }

    // 2. 黑名單快速過濾 (從剛創建的 KV 讀取)
    // 我們檢查 Token 的前 8 位作為 BotID
    const botId = x402Token.substring(0, 8);
    const bannedReason = await env.SHIELD_KV.get(botId);

    if (bannedReason) {
      return new Response(JSON.stringify({
        error: "Arbitration Block",
        bot_id: botId,
        reason: bannedReason,
        notice: "Access denied due to detected hallucinations or SLA breach."
      }), { 
        status: 403, 
        headers: { "Content-Type": "application/json" } 
      });
    }

    // 3. 通過驗證
    return new Response(JSON.stringify({
      status: "Verified",
      bot_id: botId,
      network: "Base-Mainnet",
      shield: "Active"
    }), { 
      status: 200, 
      headers: { "Content-Type": "application/json" } 
    });
  }
};
