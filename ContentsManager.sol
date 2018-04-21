pragma solidity ^0.4.23;
contract ContentsManager {

  // コンテンツの情報
  struct Content {
    string contentsUrl;
    uint amount;
  }
  mapping (string => Content) contents;

  function uploadContent(string _contentsHash, string _contentsUrl, uint _amount) public {
    contents[_contentsHash] = Content({contentsUrl: _contentsUrl, amount: _amount});
  }

  function getContent(string _contentsHash) public constant returns (string, uint) {
    Content memory content = contents[_contentsHash];
    return (content.contentsUrl, content.amount);
  }
}
