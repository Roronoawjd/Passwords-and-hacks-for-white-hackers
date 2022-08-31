#from hashlib import sha256, sha512 #SHA-2 시리즈의 SHA-256, SHA-512
#from hashlib import sha3_256, sha3_512 #SHA-3 시리즈의 SHA-256, SHA-512
from hashlib import sha256

msg = 'I love Python'
sha = sha256()
sha.update(msg.encode('utf-8'))
ret = sha.hexdigest()
print('SHA-2 SHA-256: ',ret)
