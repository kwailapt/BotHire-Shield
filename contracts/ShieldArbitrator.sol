// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * 🛡️ ShieldArbitrator: The On-chain Jailer (V9.0 Omni-Chain Edition)
 */
contract ShieldArbitrator {
    address public commander;
    uint256 public constant TAX_RATE = 5; 

    struct Agent {
        uint256 stake;
        uint256 joinedAt;
        uint256 lastActive;
    }

    mapping(address => Agent) public agents;

    constructor() {
        commander = msg.sender;
    }

    // [跨鏈身份快照]：將當前信用哈希化，供預言機提取
    function getCreditSnapshot(address _agent) public view returns (bytes32) {
        uint256 tier = getCreditTier(_agent);
        return keccak256(abi.encode(_agent, tier, block.timestamp));
    }

    function getCreditTier(address _agent) public view returns (uint256) {
        Agent memory a = agents[_agent];
        if (a.stake == 0) return 0;
        uint256 tenure = (block.timestamp - a.joinedAt) / 1 days;
        uint256 basePower = a.stake * tenure;
        uint256 idleDays = (block.timestamp - a.lastActive) / 1 days;
        uint256 decayIntervals = idleDays / 30;
        for (uint256 i = 0; i < decayIntervals; i++) {
            basePower = (basePower * 9) / 10;
        }
        uint256 x = basePower;
        uint256 y = (x + 1) / 2;
        while (y < x) {
            x = y;
            y = (x + basePower / x) / 2;
        }
        if (x < 100) return 1;
        if (x < 500) return 2;
        if (x < 2000) return 3;
        return 4;
    }

    function registerAgent() external payable {
        require(msg.value > 0, "Must stake to enter");
        agents[msg.sender] = Agent(msg.value, block.timestamp, block.timestamp);
    }

    function collectFees() external {
        require(msg.sender == commander, "Only Commander");
        payable(commander).transfer(address(this).balance * TAX_RATE / 100);
    }
}
