import json
import web3
import sys

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''

pragma solidity ^0.4.23;
contract ContentsManager {

  // コンテンツの情報
  struct Content {
    uint id;
    address creator;
    string contentsHash;
    string encryptedContentsUrl;
    string digitalSignature;
    uint amount;
  }
  // コンテンツID管理
  uint private contentId = 0;
  // コンテンツのhashをキーとしたコンテンツmapping
  mapping (string => Content) contents;
  // コンテンツのIDをキーとキーとした購入者mapping
  mapping (uint => string[]) contentsConsumer;
  // 購入者がどんなコンテンツを保持しているか
  mapping (address => Content[]) boughtContents;

  // コンテンツ登録処理
  function uploadContent(string _contentsHash, string _encryptedContentsUrl, string _digitalSignature, uint _amount) public {
    contents[_contentsHash] = Content({
      id: contentId++,
      creator: msg.sender,
      contentsHash: _contentsHash,
      encryptedContentsUrl: _encryptedContentsUrl,
      digitalSignature: _digitalSignature,
      amount: _amount
    });
  }

  // コンテンツのhashからコンテンツを検索
  function getContentForCreator(string _contentsHash) public constant returns (uint, string, uint) {
    Content memory content = contents[_contentsHash];
    require(msg.sender == content.creator);
    return (content.id, content.encryptedContentsUrl, content.amount);
  }

  function register(Content _content) private {
    boughtContents[msg.sender].push(_content);
  }

  function getBoughtContents() public constant returns (string) {
    return boughtContents[msg.sender][0].contentsHash;
  }

  function buy(string _contentsHash) public payable {
    Content memory content = contents[_contentsHash];
    content.creator.send(content.amount);
    register(contents[_contentsHash]);
  }
}
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
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
