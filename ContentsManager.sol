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

  // 暗号化したURLを購入者向けにプーリングする
  mapping (address => string) poolUrls;
  mapping (address => uint) poolBalances;

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

  function buy(string _contentsHash) private payable {
    Content memory content = contents[_contentsHash];
    if(poolBalances[msg.sendr] > content.amount)
      content.creator.send(poolBalances[msg.sender]);
      register(contents[_contentsHash]);
  }

  // 作成者が一時的に暗号化されたURLをプールする
  function poolUrl(address _consumer, string url) public {
    poolUrls[_consumer] = url;
  }

  // 一時的に支払いする
  function poolPay(uint amount) public {
    poolBalances[msg.sender] = amount;
  }

  // 支払いが行われていれば暗号化されたURLを取得できる
  function getContentsUrl(amount) public constant returns (string) {
    if ()
    )
  }
}
