from sdk.shield_governance import ShieldGovernance
from sdk.shield_ai_sentry import AISentry
from sdk.shield_executor import ShieldExecutor

# 1. 啟動組件
gov = ShieldGovernance()
sentry = AISentry()
executor = ShieldExecutor()

# 2. 發起增稅提案
gov.create_proposal("ADAPTIVE_TAX_V10", "Adaptive Tax adjustment for network stability")

# 3. AI 哨兵掃描投票者安全性 (模擬)
if sentry.analyze_behavior("0xNoble_Agent", {"stake_history": [5000, 5100]}) == "STABLE_SUBJECT":
    # 4. 投票並結算
    gov.cast_vote("ADAPTIVE_TAX_V10", "0xNoble_Agent", {"base": {"stake": 5000, "tenure": 365}}, support=True)
    
    # 5. 如果通過，自動執行
    print("\n--- 🏁 AUTOMATION SEQUENCE STARTING ---")
    executor.execute_tax_adjustment(7.5) # 根據提案自動調整至 7.5%
    print("--- ✅ EMPIRE UPDATED ---")
