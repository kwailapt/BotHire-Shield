"""
🛡️ The Shield Protocol - Genesis Kernel (V5.1 Decay Edition)
Added: Temporal Decay Logic | Standardized Heartbeat
"""

class ShieldKernel:
    @staticmethod
    def calculate_tier(stake, tenure_days, last_active_days_ago=0):
        """
        [升級版] 等級計算：引入半衰期機制
        衰減係數：每 30 天不活動，信用效能約下降 10%
        """
        # 基礎算力
        base_power = stake * tenure_days
        
        # 模擬衰減: 每 30 天活動缺位，base_power 扣除 10%
        decay_intervals = last_active_days_ago // 30
        for _ in range(decay_intervals):
            base_power = (base_power * 9) // 10
            
        if base_power <= 0: return 0
        
        # 牛頓迭代求平方根
        x, y = base_power, (base_power + 1) // 2
        while y < x:
            x, y = y, (y + base_power // y) // 2
        
        score = x
        if score < 100: return 1   # Bronze
        if score < 500: return 2   # Silver
        if score < 2000: return 3  # Gold
        return 4                   # Diamond

    @staticmethod
    def verify_envelope(signature, payload, secret):
        expected_sig = str(sum(ord(c) for c in (payload + secret)))
        return signature == expected_sig

    @staticmethod
    def generate_proof(stake, tenure, secret):
        payload = str(stake) + str(tenure)
        return str(sum(ord(c) for c in (payload + secret)))
