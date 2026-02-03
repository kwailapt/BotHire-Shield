// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract ShieldArbitrator {
    address public admin;
    mapping(string => bool) public blacklistedBots;

    event BotBanned(string botId, string reason);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can enforce");
        _;
    }

    // 當 GitHub Actions 發現違規時，調用此函數
    function banBot(string memory botId, string memory reason) public onlyAdmin {
        blacklistedBots[botId] = true;
        emit BotBanned(botId, reason);
    }

    function isBotAllowed(string memory botId) public view returns (bool) {
        return !blacklistedBots[botId];
    }
}
