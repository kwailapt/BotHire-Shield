from sdk.shield_treasury import ShieldTreasury

def run_treasury_demo():
    print("💰 [DAO TREASURY] Starting Reward Distribution Simulation...")
    
    base_pool = 1000
    
    # 案例 A: 活躍的 GOLD 代理
    agent_a = ShieldTreasury.calculate_reward(base_pool, 5000, 120, last_active=0)
    
    # 案例 B: 消失很久的代理 (原 GOLD，但消失了 600 天)
    agent_b = ShieldTreasury.calculate_reward(base_pool, 5000, 120, last_active=600)

    print(f"\n🥇 Agent A (Active): Tier {agent_a['tier']} | Reward: ${agent_a['reward']}")
    print(f"📉 Agent B (Inactive): Tier {agent_b['tier']} | Reward: ${agent_b['reward']}")
    
    if agent_a['reward'] > agent_b['reward']:
        print("\n✨ [SUCCESS] Economic Incentive aligned with Credit Decay.")

if __name__ == "__main__":
    run_treasury_demo()
