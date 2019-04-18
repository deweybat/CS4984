from urllib.request import urlopen
uurl = 'https://overrustlelogs.net/Dendi%20chatlog/April%202016/broadcaster'

def download(t_url):
    response = urlopen(t_url)
    data = response.read()
    txt_str = str(data)
    lines = txt_str.split("\\n")
    des_url = 'folder/forcast.csv'
    fx = open(des_url,"w")
    for line in lines:
        fx.write(line+ "\n")
    fx.close()

download(uurl)
