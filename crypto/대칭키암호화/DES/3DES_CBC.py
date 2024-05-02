# 단문 메시지 암호화 - 3DES CBC모드로 암호화 알고리즘
from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA
def make8String(msg):
        msglen=len(msg)
        filler=''
        if msglen%8 !=0:
            filler ='0'*(8-msglen%8)
        msg += filler
        return msg

class myDES():
    def __init__(self, keytext, ivetext):

        hash=SHA.new() # SHA256 객체를 만들고 HASH에 할당
        hash.update(keytext.encode('utf-8'))   # 주의: hash.update()는 유니코드 문자열을 인자로 받지 않음 따라서 UTF-8로 인코딩
        key = hash.digest()   # 해시 값을 추출하여 key에 할당(key는 32바이트 크기)
        self.key=key[:24]  # key를 16바이트 or 24바이트만큼 슬라이싱하여 3DES의 키로 사용

        hash.update(ivetext.encode('utf-8')) # 암호키 생성과 마찬가지로 초기화 벡터를 생성하기 위해서 SHA256 해시 사용
        iv=hash.digest()    # 해시값을 얻고 iv에 담음
        self.iv=iv[:8]      # iv의 처음 8바이트를 초기화 벡터값으로 할당

    # plaintext에 담긴 문자열을 3DES로 암호화
    def enc(self, plaintext):
        plaintext=make8String(plaintext)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)       # DES3 객체 생성(암호키, 운영모드, 초기화 벡터)
        encmsg= des3.encrypt(plaintext.encode())                # 암호화를 수행
        return encmsg
    
    # 복호화 알고리즘
    def dec(self, ciphertext):
            des3= DES3.new(self.key, DES3.MODE_CBC, self.iv)    # DES3 객체 생성
            decmsg=des3.decrypt(ciphertext)                     # 복호화를 수행
            return decmsg
    
     
def main():
    keytext='smsjang'       # 암호키
    ivetext='1234'          # 초기화 벡터를 생성하기위한 ivetext 
    msg='HIMYNAMEISJONGYUN'          # 암호화 하려는 메시지

    myCipher=myDES(keytext, ivetext)
    ciphered=myCipher.enc(msg)
    deciphered=myCipher.dec(ciphered)
    print("원본 메시지:\t%s" %msg)
    print("암호화:\t%s" %ciphered)
    print("복호화:\t%s" %deciphered)

if __name__ == '__main__':
    main()
        
