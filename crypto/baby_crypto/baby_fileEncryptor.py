
#파일 암호화 복호화 알고리즘

def makeCodebook():
    decbook={'5':'a', '2':'b', '#':'d','8':'e','1':'f','3':'g', '4':'h', '6':'i','0':'l','9':'m',\
             '*':'n', '%':'o', '=':'p','(':'r',')':'s',';':'t','?':'u','@':'v',':':'y','7':' '}
    encbook= {}
    for k in decbook:
        val =decbook[k]
        encbook[val] =k

    return encbook, decbook
def encrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg =msg.replace(c, decbook[c])
    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg= msg.replace(c, decbook[c])

    return msg

if __name__== '__main__':
    h = open('jong.txt', 'rt')     #찰리푸스 I Don't Think That I Like Her을 암호화해보기
    content=h.read()
    h.close()

    encbook, decbook= makeCodebook()
    content = encrypt(content, encbook)

    h= open('encryption.txt','wt+')
    h.write(content)
    h.close()
    