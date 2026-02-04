import requests
import time
from functools import wraps
from eth_account.messages import encode_defunct
from eth_account import Account

class ShieldGuard:
    def __init__(self, agent_address, private_key, gateway_url="https://bothire-shield-gateway.kwailapt.workers.dev"):
        self.agent_address = agent_address
        self.private_key = private_key
        self.gateway_url = gateway_url

    def _generate_x402_token(self):
        """生成符合 X-402 協議的身分證明"""
        timestamp = str(int(time.time()))
        message = f"Shield-Auth-{self.agent_address}-{timestamp}"
        msghash = encode_defunct(text=message)
        signature = Account.sign_message(msghash, private_key=self.private_key)
        return f"{self.agent_address}.{timestamp}.{signature.signature.hex()}"

    def verify_status(self):
        """向網關請求信用驗證"""
        token = self._generate_x402_token()
        headers = {"X-402-Shield-Token": token}
        try:
            response = requests.post(f"{self.gateway_url}/verify", headers=headers)
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def protect(self, min_stake=0.001, min_tenure_mins=0):
        """裝飾器：攔截不達標的 Agent 執行"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                status = self.verify_status()
                if status.get("status") != "verified":
                    raise PermissionError(f"Shield Intercepted: {status.get('message', 'Unverified')}")
                
                # 邏輯解算：Verified = (Stake >= Requirement)
                stake = float(status.get("stake", 0))
                if stake < min_stake:
                    raise PermissionError(f"Insufficient Stake: Needs {min_stake} ETH, has {stake} ETH")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
