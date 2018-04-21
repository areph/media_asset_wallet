pragma solidity ^0.4.23;
contract ContentsManager {

  // コンテンツの情報
  struct Content {
    address creator;
    string encryptedContentsUrl;
    string digitalSignature;
    uint amount;
  }
  mapping (string => Content) contents;

  function uploadContent(string _contentsHash, string _encryptedContentsUrl, string _digitalSignature, uint _amount) public {
    contents[_contentsHash] = Content({
      creator: msg.sender,
      encryptedContentsUrl: _encryptedContentsUrl,
      digitalSignature: _digitalSignature,
      amount: _amount
    });
  }

  function getContentForCreator(string _contentsHash) public constant returns (string, uint) {
    Content memory content = contents[_contentsHash];
    require(msg.sender == content.creator);
    return (content.encryptedContentsUrl, content.amount);
  }
}
