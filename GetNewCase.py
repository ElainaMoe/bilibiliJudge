import requests as r
import json as js

url='http://api.bilibili.com/x/credit/jury/caseObtain'

def GetNew(csrf,sessdata):
    headers={
        'cookie': 'bili_jct={}; SESSDATA={}'.format(csrf,sessdata),
        'Host': 'api.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }
    params={
        'csrf': csrf
    }
    data=r.post(url,headers=headers,params=params)
    dataloads=js.loads(data.text)
    # print(dataloads)
    if(dataloads['code']==25014 or dataloads['code']==25008): return True
    result=dataloads['data']['id']
    return result
