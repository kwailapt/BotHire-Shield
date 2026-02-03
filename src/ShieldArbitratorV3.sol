// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

contract ShieldArbitratorV3 {
    address public admin;
    
    // 調整後的測試門檻
    uint256 public constant SILVER_THRESHOLD = 0.0005 ether;
    uint256 public constant GOLD_THRESHOLD = 0.001 ether; 
    uint256 public constant LOYALTY_PERIOD = 1 minutes; // 測試用：1分鐘即視為長期留存

    struct AgentProfile {
        uint256 totalStaked;
        uint256 firstStakeTimestamp;
        bool isBlacklisted;
    }

    mapping(string => AgentProfile) public agents;

    constructor() { admin = msg.sender; }

    function depositStake(string memory botId) public payable {
        AgentProfile storage p = agents[botId];
        if (p.totalStaked == 0) {
            p.firstStakeTimestamp = block.timestamp;
        }
        p.totalStaked += msg.value;
        p.isBlacklisted = false;
    }

    function getAgentTier(string memory botId) public view returns (uint8) {
        AgentProfile memory p = agents[botId];
        if (p.isBlacklisted || p.totalStaked < 0.0001 ether) return 0; // Bronze

        uint256 loyaltyTime = block.timestamp - p.firstStakeTimestamp;
        
        // 錢夠 (0.001) 且 時間夠 (1min) -> Gold
        if (p.totalStaked >= GOLD_THRESHOLD && loyaltyTime >= LOYALTY_PERIOD) {
            return 2; 
        } else if (p.totalStaked >= SILVER_THRESHOLD) {
            return 1; // Silver
        }
        return 0; // Bronze
    }

    function slashAgent(string memory botId) public {
        require(msg.sender == admin, "Only admin");
        uint8 tier = getAgentTier(botId);
        if (tier == 2) {
            agents[botId].totalStaked -= (agents[botId].totalStaked / 10); // Gold 僅扣 10%
        } else {
            agents[botId].totalStaked -= (agents[botId].totalStaked / 2);  // 其他扣 50%
        }
        agents[botId].isBlacklisted = true;
    }
}
