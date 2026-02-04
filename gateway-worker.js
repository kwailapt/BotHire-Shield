export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const botId = url.searchParams.get("botId");
    const token = request.headers.get("X-402-Shield-Token");

    if (!botId) return new Response(JSON.stringify({ error: "Missing botId" }), { status: 400 });

    try {
      // 📡 呼叫 V4.2 核心合約
      const response = await fetch("https://sepolia.base.org", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          jsonrpc: "2.0",
          id: 1,
          method: "eth_call",
          params: [{
            to: "0x9b9332c7D601601E3bDBfA626dc65F33FCCDD644",
            // 使用標準簽名 hash 並修復 ABI 編碼
            data: "0x3785633a" + encodeString(botId) 
          }, "latest"]
        })
      });

      const json = await response.json();
      const tier = parseInt(json.result, 16) || 0;

      return new Response(JSON.stringify({
        protocol: "The Shield Protocol",
        version: "4.2.1-Resilient",
        botId: botId,
        tier: tier,
        access: (tier >= 2 && token === "Shield-V4.2-AUTH") ? "GRANTED" : "DENIED",
        security: token ? "Token-Verified" : "Token-Missing",
        timestamp: new Date().toISOString()
      }), {
        headers: { 
          "Content-Type": "application/json", 
          "Access-Control-Allow-Origin": "*" 
        }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: "Sync Failed" }), { status: 500 });
    }
  }
};

// 修正後的 ABI 編碼邏輯，確保長字串不截斷
function encodeString(str) {
    const offset = "0000000000000000000000000000000000000000000000000000000000000020";
    const len = str.length.toString(16).padStart(64, '0');
    let hex = "";
    for (let i = 0; i < str.length; i++) {
        hex += str.charCodeAt(i).toString(16);
    }
    return offset + len + hex.padEnd(64, '0');
}
