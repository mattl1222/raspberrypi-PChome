import requests,time
import keep_alive
def pchome():
    url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id=DSAJ2B-A900ADLET&fields=ButtonType'
    ButtonType = requests.get(url)
    if "ForSale" in ButtonType.text:
        return 1
    else:
        return 0

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
def gogo():
  while True:
    if(pchome()==1):
        lineNotifyMessage(token, '有貨了 快')
	time.sleep(60)
        break 
    time.sleep(1)

token = 'Linenotify token'

if __name__ == "__main__":
    keep_alive.keep_alive()
    gogo()
  

