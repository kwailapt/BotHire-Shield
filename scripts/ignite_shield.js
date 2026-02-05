/**
 * 🔥 Shield Protocol - Testnet Ignition Script
 * Target: Base Sepolia (ChainID: 84532)
 */

async function main() {
    console.log("📡 [IGNITION] Initializing Base Sepolia Deployment...");
    
    // 模擬部署邏輯 (適配 Hardhat 環境)
    const Shield = await ethers.getContractFactory("ShieldArbitrator");
    console.log("⚒️  Forging ShieldArbitrator on-chain...");
    
    // 部署合約
    const shield = await Shield.deploy();
    await shield.deployed();

    console.log(`✅ [SUCCESS] ShieldArbitrator deployed to: ${shield.address}`);
    console.log("🏛️  The On-chain Law is now active.");
    
    // 模擬首位 Agent 入場
    console.log("🤖 [AGENT] Simulating First Stake: 1 ETH...");
    const tx = await shield.registerAgent({ value: ethers.utils.parseEther("1.0") });
    await tx.wait();
    
    const tier = await shield.getCreditTier(tx.from);
    console.log(`📊 Agent Credit Tier verified on-chain: ${tier}`);
}

if (require.main === module) {
    main().catch((error) => {
        console.error(error);
        process.exit(1);
    });
}
