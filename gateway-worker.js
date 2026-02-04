export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const botId = url.searchParams.get("botId");

    if (!botId) return new Response(JSON.stringify({ error: "Missing botId" }), { status: 400 });

    try {
      // 📡 對接新合約地址: 0x9b9332c7D601601E3bDBfA626dc65F33FCCDD644
      const response = await fetch("https://sepolia.base.org", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          jsonrpc: "2.0",
          id: 1,
          method: "eth_call",
          params: [{
            to: "0x9b9332c7D601601E3bDBfA626dc65F33FCCDD644",
            data: "0x3785633a" + stringToHex(botId) 
          }, "latest"]
        })
      });

      const json = await response.json();
      const tier = parseInt(json.result, 16) || 0;

      return new Response(JSON.stringify({
        protocol: "The Shield Protocol",
        version: "4.2 (Resilient)",
        botId: botId,
        tier: tier,
        access: tier >= 2 ? "GRANTED" : "DENIED",
        timestamp: Date.now()
      }), {
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: "Sync Failed" }), { status: 500 });
    }
  }
};

function stringToHex(str) {
    return "0000000000000000000000000000000000000000000000000000000000000020" + 
           (str.length).toString(16).padStart(64, '0') + 
           hexEncode(str).padEnd(64, '0');
}

function hexEncode(str) {
    var hex = '';
    for(var i=0;i<str.length;i++) hex += str.charCodeAt(i).toString(16);
    return hex;
}
