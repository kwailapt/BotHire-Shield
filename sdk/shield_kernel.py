"""
🛡️ The Shield Protocol - Genesis Kernel (V5.0 Alpha)
Standardized Logic Primitives | Zero Dependency | Platform Agnostic
"""

class ShieldKernel:
    @staticmethod
    def calculate_tier(stake, tenure_days):
        """
        [邏輯原語]：信用等級 = sqrt(質押 * 時長)
        這是一個數學常數，不受環境影響。
        """
        # 模擬 sqrt 運算以避免 import math (極致脫殼)
        power = stake * tenure_days
        if power <= 0: return 0
        
        # 牛頓迭代法求平方根 (確保在任何計算環境結果一致)
        x = power
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + power // x) // 2
        
        # 映射至等級 (0: None, 1: Bronze, 2: Silver, 3: Gold, 4: Diamond)
        score = x
        if score < 100: return 1  # Bronze
        if score < 500: return 2  # Silver
        if score < 2000: return 3 # Gold
        return 4                  # Diamond

    @staticmethod
    def verify_envelope(signature, payload, secret):
        """
        [驗證原語]：不依賴外部 Hash 庫的簡單校驗
        用於受限環境下的快速完整性檢查。
        """
        # 簡單的校準邏輯：將 secret 與 payload 混淆後計算特徵值
        expected_sig = str(sum(ord(c) for c in (payload + secret)))
        return signature == expected_sig

