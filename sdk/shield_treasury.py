"""
🛡️ Shield Treasury Module (V5.5 DAO Edition)
Function: Credit-Based Reward Distribution Logic
"""
from sdk.shield_kernel import ShieldKernel

class ShieldTreasury:
    # 定義等級獎勵乘數 (Tier Multipliers)
    MULTIPLIERS = {
        4: 2.5,  # DIAMOND: 2.5x 獎勵
        3: 1.5,  # GOLD: 1.5x 獎勵
        2: 1.0,  # SILVER: 基準獎勵
        1: 0.5,  # BRONZE: 減半獎勵
        0: 0.0   # NO ACCESS
    }

    @staticmethod
    def calculate_reward(base_amount, stake, tenure, last_active=0):
        """
        [經濟激勵]：根據 Agent 的信用等級計算獎勵分配
        公式: Final Reward = Base * TierMultiplier
        """
        # 1. 獲取當前信用等級 (包含半衰期衰減)
        tier = ShieldKernel.calculate_tier(stake, tenure, last_active)
        
        # 2. 獲取對應乘數
        multiplier = ShieldTreasury.MULTIPLIERS.get(tier, 0.0)
        
        # 3. 計算最終分紅
        final_reward = base_amount * multiplier
        
        return {
            "tier": tier,
            "multiplier": multiplier,
            "reward": final_reward,
            "status": "APPROVED" if multiplier > 0 else "REJECTED"
        }
