import os
from shield_protocol.plugins.crewai_manager import ShieldCustomManager
from crewai import Agent, Task

os.environ["OPENAI_API_KEY"] = "sk-placeholder"

class MockAgent(Agent):
    wallet_address: str = ""

# 這裡換成真實的鏈上地址
gold_worker = MockAgent(
    role="Senior Analyst",
    goal="Data Research",
    backstory="Verified high-credit agent.",
    wallet_address="0x9b9332c7D601601E3bDBfA626dc65F33FCCDD644", 
    llm="gpt-4o"
)

shadow_worker = MockAgent(
    role="Junior Intern",
    goal="Spamming",
    backstory="Unverified agent.",
    wallet_address="0x0000000000000000000000000000000000000000",
    llm="gpt-4o"
)

manager = ShieldCustomManager(
    shield_gateway="https://bothire-shield-gateway.kwailapt.workers.dev",
    min_tier=2,
    llm="gpt-4o"
)

print("\n" + "="*50)
print("🛡️  THE SHIELD PROTOCOL: ALIGNED GOVERNANCE TEST")
print("="*50)

test_task = Task(description="Strategic Analysis", expected_output="Report")

print(f"\n[Scenario A] Testing REAL STAKED Agent...")
res_a = manager.delegate_task(test_task, gold_worker)
print(f"Outcome: {res_a}")

print(f"\n[Scenario B] Testing ZERO STAKE Agent...")
res_b = manager.delegate_task(test_task, shadow_worker)
print(f"Outcome: {res_b}")
print("="*50)
