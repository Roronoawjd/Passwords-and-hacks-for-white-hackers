from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

def readPEM(pemfile):
    h = open(pemfile,'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_enc(msg):
    public_key = readPEM('publickey.pem')
    cipher = PKCS1_OAEP.new(public_key)
    encdata = cipher.encrypt(msg)
    return encdata

def rsa_dec(msg):
    private_key = readPEM('privatekey.pem')
    cipher = PKCS1_OAEP.new(private_key)
    decdata = cipher.decrypt(msg)
    return decdata

def main():
    msg = 'smasjang loves python'
    ciphered = rsa_enc(msg.encode('utf-8'))
    print(ciphered)
    deciphered = rsa_dec(ciphered)
    print(deciphered)

main()