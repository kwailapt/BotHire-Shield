import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sdk.shield_kernel import ShieldKernel

def verify_incoming_agent():
    SECRET = "GLOBAL_SHIELD_SECRET"
    
    # 讀取第三方提交的憑證
    with open('tests/agent_alpha_credential.json', 'r') as f:
        packet = json.load(f)
    
    print(f"📡 [GATEWAY] Inspecting Agent from {packet['origin']['chain_id']}...")
    
    payload = str(packet['metrics']['stake']) + str(packet['metrics']['tenure'])
    
    # 執行物理層驗證
    if ShieldKernel.verify_envelope(packet['proof']['signature'], payload, SECRET):
        # 執行邏輯層裁決
        tier_code = ShieldKernel.calculate_tier(packet['metrics']['stake'], packet['metrics']['tenure'])
        tier_map = {4: "💎 DIAMOND", 3: "🥇 GOLD", 2: "🥈 SILVER", 1: "🥉 BRONZE"}
        
        print(f"✅ [SUCCESS] Signature Authentic.")
        print(f"📊 [DECISION] Agent Tier: {tier_map.get(tier_code)}")
        
        if tier_code >= 3:
            print("🔓 [ACCESS] High-level resources unlocked for Agent-Alpha.")
    else:
        print("🚨 [REJECTED] Counterfeit Credential Detected!")

if __name__ == "__main__":
    verify_incoming_agent()
