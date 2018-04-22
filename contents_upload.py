import json
import web3
import sys
import json

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from time import sleep
import gethash
import crypt

# web3.py instance
w3 = Web3(HTTPProvider('http://localhost:8545'));

# Solidity source code
with open('./contents_manager_deploy.data', "r") as f:
    deploy_info = f.read().split("\n")
contract_instance = w3.eth.contract(address=deploy_info[0], abi=json.loads(deploy_info[1]), ContractFactoryClass=ConciseContract)

# uploadConten parameter
args = sys.argv
content_hash = gethash.getHash(args[1])  # TODO コンテンツデータを元にハッシュ関数を呼び出す
encryptedContentsUrl = str(crypt.encrypt(args[2], args[3])) # TODO 引数で渡されたURLを元に暗号化関数を呼び出す
sign = "sign" # TODO 電子署名関数を呼び出す
amount = int(args[4])

contract_instance.uploadContent(content_hash, encryptedContentsUrl, sign, amount, transact={'from': w3.eth.accounts[0]})
sleep(10)
print('Contract value: {}'.format(contract_instance.getContentForCreator(content_hash)))
