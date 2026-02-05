from sdk.v11_resonance import ResonanceOracle

def induce_migration():
    oracle = ResonanceOracle()
    move_whales = [
        {"id": "0xMove_Whale_01", "stake": 900}, # 900 * 1.2 = 1080 (SUPERNOVA!)
        {"id": "0xMove_Whale_02", "stake": 2000}, # 2000 * 1.2 = 2400 (ELITE)
    ]
    
    print("📢 [BROADCAST] Scanning Move Migration Tunnel...")
    for whale in move_whales:
        res = oracle.bridge_to_move_ecosystem(whale["id"], whale["stake"])
        print(f"✅ Migration Successful: {whale['id']} | Power: {res['entangled_power']} | Status: {res['status']}")

if __name__ == "__main__":
    induce_migration()
