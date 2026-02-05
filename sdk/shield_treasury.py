"""
🛡️ Shield Treasury Module (V7.4 Diplomacy Edition)
Function: Credit-Based Rewards with Whitelist Tax Exemption
"""
from sdk.shield_kernel import ShieldKernel

class ShieldTreasury:
    MULTIPLIERS = {4: 2.5, 3: 1.5, 2: 1.0, 1: 0.5, 0: 0.0}
    TAX_RATE = 0.05
    
    # [貴族名冊]：存儲擁有豁免權的錢包地址
    WHITELIST = set()

    @classmethod
    def add_to_whitelist(cls, address):
        cls.WHITELIST.add(address)

    @staticmethod
    def calculate_reward(address, base_amount, stake, tenure, last_active=0):
        # 判斷是否擁有「外交豁免權」
        is_exempt = address in ShieldTreasury.WHITELIST
        
        # 1. 計算稅收 (豁免者稅率為 0)
        actual_tax_rate = 0 if is_exempt else ShieldTreasury.TAX_RATE
        tax_amount = base_amount * actual_tax_rate
        distributable_pool = base_amount - tax_amount
        
        # 2. 獲取信用等級
        tier = ShieldKernel.calculate_tier(stake, tenure, last_active)
        multiplier = ShieldTreasury.MULTIPLIERS.get(tier, 0.0)
        
        return {
            "address": address,
            "tier": tier,
            "is_exempt": is_exempt,
            "commander_tax": tax_amount,
            "agent_reward": distributable_pool * multiplier,
            "status": "DIPLOMATIC_IMMUNITY" if is_exempt else "TAXED"
        }
