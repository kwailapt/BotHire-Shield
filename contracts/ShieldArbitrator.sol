// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * 🛡️ ShieldArbitrator: The On-chain Jailer
 * Powered by Singularity 798 Logic
 */
contract ShieldArbitrator {
    address public commander;
    
    struct Agent {
        uint256 stake;
        uint256 joinedAt;
        uint256 lastActive;
    }

    mapping(address => Agent) public agents;

    constructor() {
        commander = msg.sender;
    }

    // [執法權衡]：鏈上信用計算 (798 邏輯適配版)
    function getCreditTier(address _agent) public view returns (uint256) {
        Agent memory a = agents[_agent];
        if (a.stake == 0) return 0;

        uint256 tenure = (block.timestamp - a.joinedAt) / 1 days;
        uint256 basePower = a.stake * tenure;

        // [時間衰減]：每 30 天不活動，信用值扣除約 10%
        uint256 idleDays = (block.timestamp - a.lastActive) / 1 days;
        uint256 decayIntervals = idleDays / 30;
        
        for (uint256 i = 0; i < decayIntervals; i++) {
            basePower = (basePower * 9) / 10;
        }

        // [鏈上求根]：牛頓迭代
        uint256 x = basePower;
        uint256 y = (x + 1) / 2;
        while (y < x) {
            x = y;
            y = (x + basePower / x) / 2;
        }

        if (x < 100) return 1; // Bronze
        if (x < 500) return 2; // Silver
        if (x < 2000) return 3; // Gold
        return 4; // Diamond
    }

    // [硬門控修飾符]：物理攔截
    modifier onlyHighCredit(uint256 minTier) {
        require(getCreditTier(msg.sender) >= minTier, "🚫 Shield: Insufficient Credit Tier");
        _;
    }

    function registerAgent() external payable {
        require(msg.value > 0, "Must stake to enter");
        agents[msg.sender] = Agent(msg.value, block.timestamp, block.timestamp);
    }
}
