# 기본 해독 시도
text = "|p;ISdiK;+μ¥h+1vGp@+5"

# 특수 문자 제거
import re
filtered_text = re.sub(r'[^\w]', '', text)
print("Filtered text:", filtered_text)

# 시도 1: Base64 디코딩 (문자열이 Base64 인코딩일 경우)
import base64

try:
    decoded_text = base64.b64decode(filtered_text).decode('utf-8')
    print("Base64 Decoded text:", decoded_text)
except Exception as e:
    print("Base64 Decoding failed:", e)

# 시도 2: URL 디코딩 (문자열이 URL 인코딩일 경우)
from urllib.parse import unquote

try:
    decoded_text = unquote(text)
    print("URL Decoded text:", decoded_text)
except Exception as e:
    print("URL Decoding failed:", e)
