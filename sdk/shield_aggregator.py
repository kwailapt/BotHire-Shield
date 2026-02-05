"""
🛡️ Shield Aggregate Credit Engine (V9.2)
Logic: Summing stakes across all colonies (Base, Monad, Arbitrum)
"""

class ShieldAggregator:
    def __init__(self, commander_tax=0.05):
        self.tax_rate = commander_tax

    def aggregate_global_credit(self, multi_chain_data):
        """
        multi_chain_data: 格式為 {'chain_name': {'stake': value, 'tenure': days}}
        """
        total_stake = 0
        max_tenure = 0
        
        print(f"📊 [AGGREGATING] Scanning global footprint...")
        
        for chain, data in multi_chain_data.items():
            stake = data.get('stake', 0)
            tenure = data.get('tenure', 0)
            total_stake += stake
            # 資歷取其最久者，代表 Agent 在帝國的忠誠起點
            if tenure > max_tenure:
                max_tenure = tenure
            print(f"  - {chain.upper()}: Stake {stake} | Tenure {tenure} days")

        # 核心 798 聚合公式：Score = sqrt(Sum(Stakes) * Max(Tenure))
        raw_power = total_stake * max_tenure
        
        # 模擬 EVM 求根 (Newton Method)
        x = raw_power
        if x > 0:
            y = (x + 1) // 2
            while y < x:
                x, y = y, (x + raw_power // y) // 2
        
        # 判定全球等級 (Global Tier)
        if x >= 2000: tier = 4   # Diamond
        elif x >= 500: tier = 3  # Gold
        elif x >= 100: tier = 2  # Silver
        else: tier = 1           # Bronze
        
        return {
            "global_tier": tier,
            "total_stake": total_stake,
            "max_tenure": max_tenure,
            "aggregate_score": x
        }

if __name__ == "__main__":
    aggregator = ShieldAggregator()
    
    # 模擬一個跨鏈 Agent 的資產分布
    agent_portfolio = {
        "base": {"stake": 1200, "tenure": 45},
        "monad": {"stake": 800, "tenure": 10},
        "arbitrum": {"stake": 500, "tenure": 5}
    }
    
    result = aggregator.aggregate_global_credit(agent_portfolio)
    
    print("-" * 40)
    print(f"🏆 [GLOBAL RESULT] Global Tier: {result['global_tier']}")
    print(f"🔥 Aggregate Power: {result['aggregate_score']}")
    print(f"🏛️  Verdict: {'Promote to Diamond' if result['global_tier'] == 4 else 'Maintain Status'}")
