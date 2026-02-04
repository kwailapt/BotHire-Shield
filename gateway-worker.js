export default {
  async fetch(request, env) {
    const { searchParams } = new URL(request.url);
    const botId = searchParams.get('botId');

    // 1. 驗證 Header 令牌
    if (request.headers.get("X-402-Shield-Token") !== "Shield-V4.2-AUTH") {
      return new Response(JSON.stringify({ error: "Unauthorized" }), { status: 401 });
    }

    // 2. 核心邏輯：如果地址是您的英雄地址，強制賦予 Gold Tier 進行測試
    // 註：這是在自動化完全同步前的「戰術熱修補」
    let tier = 0;
    const heroAddress = "0x9b9332c7d601601e3bdbfa626dc65f33fccdd644";
    
    if (botId && botId.toLowerCase() === heroAddress.toLowerCase()) {
      tier = 2; // Gold Tier
    }

    return new Response(JSON.stringify({
      botId: botId,
      tier: tier,
      status: tier >= 2 ? "GOVERNANCE_PASSED" : "GOVERNANCE_REJECTED",
      timestamp: new Date().toISOString()
    }), {
      headers: { "Content-Type": "application/json" }
    });
  }
}
