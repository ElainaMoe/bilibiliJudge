import requests as r
import json as js

url='http://api.bilibili.com/x/credit/jury/caseObtain'

def GetNew(csrf):
    headers={
        'cookie': 'bili_jct={}'.format(csrf)
    }
    data=r.post(url,headers=headers)
    dataloads=js.loads(data.text)
    result=dataloads['data']['id']
    return result