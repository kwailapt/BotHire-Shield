import time
from sdk.shield_parallel import ShieldParallel

def run_stress_test():
    # 模擬 10,000 個併發 Agent 數據
    mock_agents = [{"stake": 5000, "tenure": 120, "last_active": 0} for _ in range(10000)]
    
    start_time = time.time()
    
    # 執行批次並行校驗
    results = ShieldParallel.batch_calculate(mock_agents)
    
    end_time = time.time()
    
    print(f"⚡ [MONAD TEST] Processed {len(results)} Agents.")
    print(f"⏱️ [PERFORMANCE] Time Taken: {end_time - start_time:.4f} seconds.")
    print(f"🚀 [THROUGHPUT] {len(results)/(end_time - start_time):.0f} Validations/sec")

if __name__ == "__main__":
    run_stress_test()
