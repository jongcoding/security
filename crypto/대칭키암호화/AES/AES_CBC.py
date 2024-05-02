# AES 단순 메시지 암호화 알고리즘

from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    
    def __init__(self, keytext, ivetext):
        hash=SHA.new()
        hash.update(keytext.encode('utf-8'))
        key=hash.digest()
        self.key=key[:16]

        hash.update(ivetext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:16]
    
    def makeEnabled(self, plaintext):
        fillersize=0
        textsize= len(plaintext)

        if textsize%16 != 0:
            fillersize=16-textsize%16
        filler='0'*fillersize
        header ='%d' %(fillersize)
        gap=16-len(header)
        header += '#'*gap

        return header+plaintext+filler
    
    # 암호화 알고리즘
    def enc(self, plaintext):
        plaintext =self.makeEnabled(plaintext)
        aes=AES.new(self.key, AES.MODE_CBC, self.iv)
        encmsg= aes.encrypt(plaintext.encode())
        return encmsg
    
    # 복호화 알고리즘
    def dec(self, ciphertext):
        aes =AES.new(self.key, AES.MODE_CBC, self.iv)
        decmsg=aes.decrypt(ciphertext)

        header= decmsg[:16].decode()
        fillersize= int(header.split('#')[0])
        if fillersize != 0:
            decmsg= decmsg[16:-fillersize]
        else:
            decmsg=decmsg[16:]
        return decmsg
def main():
    keytext='smsjang'       # 암호키
    ivetext='1234'          # 초기화 벡터를 생성하기위한 ivetext 
    msg='HIMYNAMEISJONGYUN'          # 암호화 하려는 메시지

    myCipher=myAES(keytext, ivetext)
    ciphered=myCipher.enc(msg)
    deciphered=myCipher.dec(ciphered)
    print("원본 메시지:\t%s" %msg)
    print("암호화:\t%s" %ciphered)
    print("복호화:\t%s" %deciphered)

if __name__ == '__main__':
    main()