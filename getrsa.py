from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

#Create the rsa crypt url from pubkey
def exportRSA(pubkey, URL):
  public_pem = open(pubkey).read()
  url = URL.encode('utf-8')

  cipher = PKCS1_OAEP.new(RSA.importKey(public_pem))
  cipher_text = cipher.encrypt(url)
  
  return cipher_text

#cipher = PKCS1_OAEP.new(RSA.importKey(private_pem))
#print("秘密鍵による復号化", int(time.time()*1000-start), 'mSec', cipher.decrypt(cipher_text))
