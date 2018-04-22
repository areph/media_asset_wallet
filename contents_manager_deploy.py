import json
import web3
import sys
import json

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from time import sleep

# Solidity source code
with open("./ContentsManager.sol", "r") as f:
    contents_manager_code = f.read()

compiled_sol = compile_source(contents_manager_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:ContentsManager']

# web3.py instance
w3 = Web3(HTTPProvider('http://localhost:8545'));

# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 4000000})
blockNumber=w3.eth.blockNumber
sleep(20)

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
abi = contract_interface['abi']

with open("./contents_manager_deploy.data", "w") as f:
    f.write(contract_address + "\n" + json.dumps(abi))
