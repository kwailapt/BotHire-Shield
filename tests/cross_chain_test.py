import sys
import os

# 將 sdk 加入路徑
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sdk.shield_kernel import ShieldKernel

def run_cross_chain_test():
    print("🚀 [TEST] Starting Cross-Chain Logic Verification...")
    
    # 定義通訊密鑰 (必須與驗證端一致)
    SECRET = "SECRET"
    
    # 模擬 Solana 數據
    stake = 5000
    tenure = 120
    payload = str(stake) + str(tenure)
    
    # [修正點]：根據 Kernel 算法生成正確簽名
    # Kernel 算法是: str(sum(ord(c) for c in (payload + secret)))
    correct_sig = str(sum(ord(c) for c in (payload + SECRET)))

    solana_packet = {
        "origin": {"chain_id": "solana:mainnet"},
        "metrics": {"stake": stake, "tenure": tenure},
        "proof": {"signature": correct_sig}
    }

    print(f"📡 Received Packet from: {solana_packet['origin']['chain_id']}")
    print(f"🔑 Expected Sig: {correct_sig}")

    # 執行驗證
    is_valid = ShieldKernel.verify_envelope(
        solana_packet['proof']['signature'], 
        payload,
        SECRET
    )
    
    if is_valid:
        print("✅ Envelope Integrity Verified.")
        tier = ShieldKernel.calculate_tier(stake, tenure)
        tier_names = {1: "BRONZE", 2: "SILVER", 3: "GOLD", 4: "DIAMOND"}
        print(f"🏆 Final Credit Decision: {tier_names.get(tier)}")
        print("\n✨ TEST PASSED: Cross-chain trust established.")
    else:
        print("❌ Security Breach: Invalid Signature.")

if __name__ == "__main__":
    run_cross_chain_test()
