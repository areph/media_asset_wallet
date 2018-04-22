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


#tradeContent parameter
args = sys.argv
content_hash = gethash.getHash(args[1])　# コンテンツHashデータを取得
cryptUrl  = contract_instance.getContentForCorCreator(content_hash)
decryptedContentsUrl = str(crypt.decrypt(args[2], cryptUrl[1])) #引数で渡された暗号化URLを復号化する
payment = float(args[2])


contract_instance.(content_hash, decryptContentsUrl, payment={'from' w3.eth.accounts[0]})
sleep(10)
