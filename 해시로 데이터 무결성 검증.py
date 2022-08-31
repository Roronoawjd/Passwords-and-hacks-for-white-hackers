from hashlib import sha256

def Hash(msg):
    sha = sha256()
    sha.update(msg.encode('utf-8'))
    ret = sha.hexdigest()
    return ret

def Hash_Check(msg1, msg2):
    msg1 = Hash(msg1)
    msg2 = Hash(msg2)

    print('msg1 = %s' %msg1,'msg2 = %s' %msg2,sep='\n')
    if msg1 == msg2:
        print('same string')
    else:
        print('not same string')
        
def main():
    msg1 = 'leejeongwoo handsome'
    msg2 = 'leejeongwoo handsomo'
    Hash_Check(msg1, msg2)
    
main()