// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransactionContract {
    struct Transaction {
        address sender;
        address receiver;
        uint amount;
        uint timestamp;
    }

    Transaction[] public transactions;

    event TransactionMade(address indexed sender, address indexed receiver, uint amount, uint timestamp);

    function makeTransaction(address _receiver, uint _amount) public {
        transactions.push(Transaction(msg.sender, _receiver, _amount, block.timestamp));
        emit TransactionMade(msg.sender, _receiver, _amount, block.timestamp);
    }

    function getTransactions() public view returns (Transaction[] memory) {
        return transactions;
    }
}

