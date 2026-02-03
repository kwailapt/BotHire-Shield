// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

contract ShieldArbitratorV2 {
    address public admin;
    uint256 public constant MIN_STAKE = 0.001 ether; // 最低質押門檻
    uint256 public constant SLASH_AMOUNT = 0.0005 ether; // 違規罰金

    mapping(string => uint256) public botStakes;
    mapping(string => bool) public isBlacklisted;

    event Staked(string botId, uint256 amount);
    event Slashed(string botId, uint256 penalty, string reason);
    event Reinstated(string botId);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can enforce");
        _;
    }

    // 1. Bot 質押資金以獲取「信任額度」
    function depositStake(string memory botId) public payable {
        require(msg.value >= MIN_STAKE, "Stake below minimum requirement");
        botStakes[botId] += msg.value;
        isBlacklisted[botId] = false; // 質押即視為嘗試修復信用
        emit Staked(botId, msg.value);
    }

    // 2. 執法邏輯：扣除罰金並列入黑名單
    function slashBot(string memory botId, string memory reason) public onlyAdmin {
        require(botStakes[botId] > 0, "No stake to slash");
        
        uint256 penalty = botStakes[botId] >= SLASH_AMOUNT ? SLASH_AMOUNT : botStakes[botId];
        botStakes[botId] -= penalty;
        isBlacklisted[botId] = true;

        emit Slashed(botId, penalty, reason);
    }

    // 3. 自我修復查詢：只有質押充足且不在黑名單才算 Allowed
    function isBotAllowed(string memory botId) public view returns (bool) {
        return (botStakes[botId] >= MIN_STAKE && !isBlacklisted[botId]);
    }

    // 提取罰金池（僅限管理員，用於協議維護）
    function withdrawFees() public onlyAdmin {
        payable(admin).transfer(address(this).balance);
    }
}
