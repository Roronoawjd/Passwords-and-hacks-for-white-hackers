from hashlib import sha256 as SHA
SIZE = 1024*256 #256K 정의

def getFileHash(filename):
    sha = SHA()
    h = open(filename,'rb')
    content = h.read(SIZE)  # 파일에서 256KB만큼 읽음
    while content:
        sha.update(content) # 읽은 256KB 정보만큼 해시할 데이터 갱신
        content = h.read(SIZE) # 파일에서 그 다음 256KB 읽음
    h.close()

    hashval = sha.digest()  # 최종 해시값 계산
    return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)

    if hashval1 == hashval2:
        print('Two files are Same')
    else:
        print('Two files are Different')

def main():
    file1 = 'plain.txt'
    file2 = 'plain.txt.enc.dec'
    hashCheck(file1,file2)

main()