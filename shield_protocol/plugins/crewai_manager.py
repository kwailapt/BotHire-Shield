from crewai import Agent, Task
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ShieldProtocol")

class ShieldCustomManager(Agent):
    def __init__(self, shield_gateway: str, min_tier: int = 2, *args, **kwargs):
        # 1. 使用 Pydantic 兼容的方式初始化基礎類
        if 'role' not in kwargs: kwargs['role'] = "The Shield Sentinel Manager"
        if 'goal' not in kwargs: kwargs['goal'] = "Maintain high-credit task security."
        if 'backstory' not in kwargs: kwargs['backstory'] = "V4.2 Governance Engine."
        
        super().__init__(*args, **kwargs)
        
        # 2. 強制注入非 Pydantic 欄位 (繞過 ValueError)
        object.__setattr__(self, 'shield_gateway', shield_gateway)
        object.__setattr__(self, 'min_tier', min_tier)

    def validate_agent_credit(self, agent: Agent) -> bool:
        # 安全獲取錢包地址
        address = getattr(agent, 'wallet_address', None)
        if not address:
            logger.error(f"🚫 [Shield] Agent {agent.role} has no wallet_address field.")
            return False

        try:
            # 呼叫 V4.2 網關
            response = requests.get(
                f"{self.shield_gateway}/?botId={address}",
                headers={"X-402-Shield-Token": "Shield-V4.2-AUTH"},
                timeout=5
            )
            data = response.json()
            current_tier = data.get("tier", 0)
            
            if response.status_code == 200 and current_tier >= self.min_tier:
                logger.info(f"✅ [Shield] Agent {agent.role} Verified. Tier: {current_tier}")
                return True
            else:
                logger.warning(f"🚫 [Shield] Agent {agent.role} Rejected. Tier {current_tier} < {self.min_tier}")
                return False
        except Exception as e:
            logger.error(f"⚠️ [Shield] Gateway connection error: {e}")
            return False

    def delegate_task(self, task: Task, agent: Agent):
        # 核心攔截邏輯
        if self.validate_agent_credit(agent):
            return f"Success: Task '{task.description}' assigned to {agent.role}."
        else:
            return f"Denied: Access Revoked for {agent.role} due to low credit."
