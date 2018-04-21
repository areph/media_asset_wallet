import json
import web3
import sys

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contents_manager_code = open('./ContentsManager.sol').read()

compiled_sol = compile_source(contents_manager_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:ContentsManager']

# web3.py instance
w3 = Web3(TestRPCProvider())

# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 4000000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
abi = contract_interface['abi']
contract_instance = w3.eth.contract(address=contract_address, abi=abi,ContractFactoryClass=ConciseContract)

# uploadConten parameter
args = sys.argv
content_hash = "0xa"  # TODO コンテンツデータを元にハッシュ関数を呼び出す
encryptedContentsUrl = "http://hoge" # TODO 引数で渡されたURLを元に暗号化関数を呼び出す
sign = "sign" # TODO 電子署名関数を呼び出す
amount = 20 #args[3]

contract_instance.uploadContent(content_hash, encryptedContentsUrl, sign, amount, transact={'from': w3.eth.accounts[0]})
print('Contract value: {}'.format(contract_instance.getContentForCreator(content_hash)))
