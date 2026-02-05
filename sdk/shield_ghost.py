# 🛡️ Shield Ghost SDK (V5.1) - The Invisible Protector
# One file. Zero dependency. Absolute trust.

SECRET = "SET_YOUR_BOT_SECRET_HERE"

def check_access(stake, tenure, days_ago=0, min_tier=2):
    """
    [幽靈門控]：一鍵驗證 Agent 是否具備訪問權限
    """
    # 1. 核心代謝算法 (Metabolism)
    p = stake * tenure
    for _ in range(days_ago // 30): p = (p * 9) // 10
    if p <= 0: return False
    
    # 2. 快速求根
    x, y = p, (p + 1) // 2
    while y < x: x, y = y, (y + p // y) // 2
    
    # 3. 門控判定 (預設 SILVER 以上可通行)
    score = x
    tier = 1 if score < 100 else (2 if score < 500 else (3 if score < 2000 else 4))
    return tier >= min_tier

def verify_packet(packet, secret=SECRET):
    """
    [幽靈校驗]：驗證外部傳入封包的完整性
    """
    payload = str(packet.get('stake', 0)) + str(packet.get('tenure', 0))
    expected = str(sum(ord(c) for c in (payload + secret)))
    return packet.get('signature') == expected
