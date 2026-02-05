"""
🧠 Shield AI Sentry (V10.0)
Logic: Behavioral Anomaly Detection for Agents
"""

class AISentry:
    def __init__(self, sensitivity=0.8):
        self.sensitivity = sensitivity
        self.threat_log = []

    def analyze_behavior(self, agent_address, historical_data):
        """
        分析 Agent 行為：如果質押量突然大幅波動或資歷異常，標記為威脅。
        """
        stake_changes = historical_data.get('stake_history', [])
        
        # 簡單的神經網路邏輯模擬：檢測「閃電貸質押」特徵
        if len(stake_changes) > 1:
            volatility = abs(stake_changes[-1] - stake_changes[-2]) / stake_changes[-2]
            if volatility > self.sensitivity:
                print(f"🚨 [AI ALERT] Anomaly detected for {agent_address[:10]}!")
                print(f"🚩 Reason: High Stake Volatility ({volatility*100:.1f}%)")
                return "THREAT_DETECTED"
        
        return "STABLE_SUBJECT"

if __name__ == "__main__":
    sentry = AISentry()
    
    # 模擬一個可疑的 Agent (突然質押 10,000 ETH 又撤回)
    suspicious_agent = {
        "stake_history": [10, 10000] # 典型的閃電貸操控信用行為
    }
    
    verdict = sentry.analyze_behavior("0xAttacker_Address", suspicious_agent)
    print(f"🧠 AI Sentry Verdict: {verdict}")
