from hashlib import md5

username = b"admin"
ip_addr = b"127.0.0.1"
csrf_token = md5("5f4dcc3b5aa765d61d8327deb882cf99").hexdigest()
print(csrf_token)