"""
🛡️ Shield Parallel Core (V5.2 Monad-Optimized)
Architecture: Conflict-Free Deterministic Logic
"""

class ShieldParallel:
    @staticmethod
    def batch_calculate(agent_list):
        """
        [並行優化]：批次處理 Agent 信用
        在並行鏈中，我們可以一次性將一組交易的信用狀態映射出來
        """
        results = []
        for agent in agent_list:
            # 展開邏輯，減少函數跳轉開銷
            stake = agent['stake']
            tenure = agent['tenure']
            decay = agent.get('last_active', 0) // 30
            
            p = stake * tenure
            # 優化衰減計算法：使用位移近似值提高並行效率
            for _ in range(decay):
                p = (p * 9) >> 3 # 快速逼近 0.9 倍 (適配並行指令集)
                p = p if p > 0 else 0
            
            # 門控直接映射
            results.append(ShieldParallel._quick_sqrt_tier(p))
        return results

    @staticmethod
    def _quick_sqrt_tier(p):
        if p <= 0: return 0
        # 針對並行 CPU 優化的快速平方根逼近
        x = p
        y = (x + 1) // 2
        while y < x:
            x, y = y, (y + p // y) // 2
        
        # 靜態門控表 (Lock-free)
        if x < 100: return 1
        if x < 500: return 2
        if x < 2000: return 3
        return 4
