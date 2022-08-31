def makecodebook():
    decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l'\
    , '9':'m', '*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
    
    encbook = {}
    for key in decbook:
        value = decbook[key]
        encbook[value] = key
    
    return encbook, decbook

def encrypt(msg, encbook):
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])

    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])
    
    return msg

if __name__ == '__main__':
    plaintext = 'I love you with all my heart'

    encbook, decbook = makecodebook()
    ciphertext = encrypt(plaintext, encbook)
    print(ciphertext)

    deciphertext = decrypt(ciphertext, decbook)
    print(deciphertext)