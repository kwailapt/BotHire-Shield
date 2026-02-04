// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract ShieldArbitrator {
    struct Agent {
        uint256 balance;
        uint256 startTime;
        bool isActive;
    }

    mapping(string => Agent) public agents;
    address public judge;

    constructor() { judge = msg.sender; }

    // V4.2 強化版：允許被 Slash 的 Bot 透過足額質押立即重啟
    function stake(string memory botId) public payable {
        require(msg.value >= 0.001 ether, "Insufficient stake");
        
        // 如果是新質押或被 Slash 後重啟
        if (agents[botId].balance == 0) {
            agents[botId].startTime = block.timestamp;
            agents[botId].isActive = true;
        }
        
        agents[botId].balance += msg.value;
    }

    function getAgentTier(string memory botId) public view returns (uint256) {
        Agent memory a = agents[botId];
        if (!a.isActive || a.balance < 0.001 ether) return 0;
        if (block.timestamp - a.startTime > 60) return 2; // Gold Tier (60s tenure)
        return 1; // Silver Tier
    }

    function slashAgent(string memory botId) public {
        require(msg.sender == judge, "Only judge can slash");
        agents[botId].balance = 0;
        agents[botId].isActive = false;
        // 移除 startTime 以重置信用
        agents[botId].startTime = 0;
    }
}
