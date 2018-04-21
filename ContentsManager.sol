pragma solidity ^0.4.23;
contract ContentsManager {

  // コンテンツの情報
  struct Content {
    uint id;
    address creator;
    string encryptedContentsUrl;
    string digitalSignature;
    uint amount;
  }
  uint private contentId = 0;
  mapping (string => Content) contents;
  mapping (uint => string[]) contentsConsumer;

  function uploadContent(string _contentsHash, string _encryptedContentsUrl, string _digitalSignature, uint _amount) public {
    contents[_contentsHash] = Content({
      id: contentId++,
      creator: msg.sender,
      encryptedContentsUrl: _encryptedContentsUrl,
      digitalSignature: _digitalSignature,
      amount: _amount
    });
  }

  function getContentForCreator(string _contentsHash) public constant returns (uint, string, uint) {
    Content memory content = contents[_contentsHash];
    require(msg.sender == content.creator);
    return (content.id, content.encryptedContentsUrl, content.amount);
  }

}
