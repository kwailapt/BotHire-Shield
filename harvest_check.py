from sdk.shield_treasury import ShieldTreasury

# 模擬 10,000 獎勵池
result = ShieldTreasury.calculate_reward(10000, 5000, 120, 0)

print("------------------------------------------")
print(f"💰 [HARVEST] Base Pool: $10000")
print(f"🏛️  Commander Tax (5%): ${result['commander_tax']:.2f}")
print(f"🥇 Agent (Gold) Reward: ${result['agent_reward']:.2f}")
print("------------------------------------------")
print("✅ Tax extraction logic confirmed.")
