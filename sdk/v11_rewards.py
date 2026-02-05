"""
🌌 Shield Resonance Rewards (V11.1)
Logic: Distributing dividends based on Cross-chain Aggregate Power.
"""
from sdk.v11_resonance import ResonanceOracle

class ResonanceRewards(ResonanceOracle):
    def __init__(self, multiplier=0.15):
        super().__init__()
        self.reward_multiplier = multiplier

    def calculate_resonance_bonus(self, agent_address, multi_chain_scores):
        """
        [中]: 根據共鳴功率發放跨鏈紅利，強化引力。
        [EN]: Issue resonance bonuses based on aggregate power to strengthen gravity.
        """
        # 1. 獲取共鳴狀態
        state = self.entangle_state(agent_address, multi_chain_scores)
        power = state["entangled_power"]
        
        # 2. 計算共鳴紅利 (具備階梯式激勵)
        if power >= 1000:
            tier = "SUPERNOVA"
            bonus = power * self.reward_multiplier * 2  # 頂級 Agent 雙倍收益
        else:
            tier = "STAR"
            bonus = power * self.reward_multiplier
            
        print(f"💎 [DIVIDEND] Agent {agent_address[:10]} categorized as [{tier}].")
        print(f"💰 [REWARD] Issued {bonus:.2f} SHIELD-DROPS across the Resonance Field.")
        
        return {"tier": tier, "bonus": bonus}

if __name__ == "__main__":
    reward_engine = ResonanceRewards()
    
    # 測試 A：星系級 Agent (1000 點功率)
    print("--- Testing Supernova Agent ---")
    reward_engine.calculate_resonance_bonus("0xCommander_Agent", {"base": 500, "monad": 500})
    
    print("\n" + "-"*35 + "\n")
    
    # 測試 B：普通 Agent (300 點功率)
    print("--- Testing Standard Agent ---")
    reward_engine.calculate_resonance_bonus("0xStandard_Agent", {"base": 200, "monad": 100})
