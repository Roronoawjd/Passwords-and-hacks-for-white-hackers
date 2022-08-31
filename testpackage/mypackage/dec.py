import enc

def decryption():
    print('Decryption')

if __name__=='__main___':
    print('dec.py가 메인임')
    enc.encryption()
    decryption()
else:
    print('dec.py가 다른 모듈에서 임포트되어 사용됨')