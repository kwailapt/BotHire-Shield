from sdk.shield_treasury import ShieldTreasury

# 1. 註冊一位貴族
noble_address = "0x798_VIP_ALLY"
ShieldTreasury.add_to_whitelist(noble_address)

# 2. 對比測試
commoner = ShieldTreasury.calculate_reward("0x123_COMMON", 10000, 5000, 120, 0)
noble = ShieldTreasury.calculate_reward(noble_address, 10000, 5000, 120, 0)

print(f"👤 Commoner Tax: ${commoner['commander_tax']:.2f} | Net Reward: ${commoner['agent_reward']:.2f}")
print(f"👑 Noble Tax:    ${noble['commander_tax']:.2f} | Net Reward: ${noble['agent_reward']:.2f}")

if noble['agent_reward'] > commoner['agent_reward']:
    print("\n✨ [SUCCESS] Diplomatic Immunity confirmed. Nobles receive 100% pool benefits.")
