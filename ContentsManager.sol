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

}
