"""
⚡ Shield Circuit Breaker Logic (Safety Protocol)
Purpose: Prevent catastrophic parameter changes by enforcing a ±50% safety corridor.
"""

def execute_tax_adjustment_demo(new_rate):
    # 基準稅率設定為 5.0%
    baseline = 5.0
    
    # 計算偏差率：(新稅率 - 基準) / 基準
    deviation = abs(new_rate - baseline) / baseline
    
    print(f"🔍 [SCANNING] Analyzing proposed tax rate: {new_rate}%")
    
    if deviation > 0.5:
        # 偏差超過 50%，觸發強制鎖定
        print(f"🚨 [CIRCUIT BREAKER] Proposed rate {new_rate}% exceeds safety threshold (Max deviation: 50%)!")
        print("🔒 [LOCKDOWN] Manual Commander authorization required. Execution halted.")
        return False
    
    # 在安全範圍內，允許修改
    print(f"✅ [ADJUSTMENT APPROVED] Tax rate updated to {new_rate}%.")
    return True

if __name__ == "__main__":
    print("--- 🛡️ Circuit Breaker Stress Test ---")
    
    # 測試 A：安全範圍內的調整 (7.5%)
    execute_tax_adjustment_demo(7.5)
    
    print("\n" + "-"*30 + "\n")
    
    # 測試 B：觸發熔斷的惡意調整 (10.0%)
    execute_tax_adjustment_demo(10.0)
