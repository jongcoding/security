from hashlib import md5

username = b"admin"
ip_addr = b"127.0.0.1"
csrf_token = md5(username + ip_addr).hexdigest()
print(csrf_token)