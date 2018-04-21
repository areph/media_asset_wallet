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
