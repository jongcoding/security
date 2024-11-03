from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# 복호화에 필요한 데이터
key = bytes.fromhex('06EB00670000000006EB006700000000')  # 주어진 16바이트 키 (AES-128)
iv = bytes.fromhex('7FFC397E382D1A6B0F20442F368C527B')   # 주어진 16바이트 IV
input_filename = 'GWbmXmlET9YAP4lE'  # 암호화된 데이터가 저장된 파일 이름

# 파일에서 암호화된 데이터 읽기
with open(input_filename, 'rb') as f:
    ciphertext = f.read()

# AES-128 CBC 모드 설정
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()

# 복호화 진행
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

# 패딩 제거 함수
def unpad(data):
    pad_length = data[-1]  # 마지막 바이트를 사용하여 패딩 길이 결정
    return data[:-pad_length]  # 패딩 제거

# 복호화 후 패딩 제거
decrypted_plaintext = unpad(decrypted_padded)

# 복호화된 데이터 출력
print(f'복호화된 데이터: {decrypted_plaintext.decode()}')
