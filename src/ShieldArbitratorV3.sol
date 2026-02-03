// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

contract ShieldArbitratorV3 {
    address public admin;
    
    // 定義等級門檻 (以 Wei 為單位)
    uint256 public constant SILVER_THRESHOLD = 0.005 ether;
    uint256 public constant GOLD_THRESHOLD = 0.01 ether;
    uint256 public constant LOYALTY_PERIOD = 30 days;

    struct AgentProfile {
        uint256 totalStaked;
        uint256 firstStakeTimestamp;
        uint256 lastViolationTimestamp;
        bool isBlacklisted;
    }

    mapping(string => AgentProfile) public agents;

    constructor() { admin = msg.sender; }

    // 質押與等級提升
    function depositStake(string memory botId) public payable {
        AgentProfile storage p = agents[botId];
        if (p.totalStaked == 0) {
            p.firstStakeTimestamp = block.timestamp;
        }
        p.totalStaked += msg.value;
        p.isBlacklisted = false;
    }

    // 動態計算等級：結合「錢」與「時間」
    function getAgentTier(string memory botId) public view returns (uint8) {
        AgentProfile memory p = agents[botId];
        if (p.isBlacklisted || p.totalStaked < 0.001 ether) return 0; // Bronze

        uint256 loyaltyTime = block.timestamp - p.firstStakeTimestamp;
        
        if (p.totalStaked >= GOLD_THRESHOLD && loyaltyTime >= LOYALTY_PERIOD) {
            return 2; // Gold
        } else if (p.totalStaked >= SILVER_THRESHOLD) {
            return 1; // Silver
        }
        return 0; // Bronze
    }

    // 階級化懲罰：高等級 Bot 擁有更高的「信用容錯率」
    function slashAgent(string memory botId) public {
        require(msg.sender == admin, "Only admin");
        uint8 tier = getAgentTier(botId);
        
        if (tier == 2) {
            agents[botId].totalStaked -= (agents[botId].totalStaked / 10); // Gold 僅扣 10%
        } else {
            agents[botId].totalStaked -= (agents[botId].totalStaked / 2);  // 其他扣 50%
        }
        agents[botId].isBlacklisted = true;
        agents[botId].lastViolationTimestamp = block.timestamp;
    }
}
