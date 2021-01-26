import requests as r
import json as js

url='http://api.bilibili.com/x/credit/jury/caseObtain'

def GetNew(csrf,sessdata):
    headers={
        'cookie': 'bili_jct={}; SESSDATA={}'.format(csrf,sessdata)
    }
    params={
        'csrf': csrf
    }
    data=r.post(url,headers=headers,params=params)
    dataloads=js.loads(data.text)
    if(dataloads['code']==25014): return True
    result=dataloads['data']['id']
    return result