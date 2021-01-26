import requests as r

url='http://api.bilibili.com/x/credit/jury/caseObtain'

def GetNew(csrf):
    headers={
        'cookie': 'bili_jct={}'.format(csrf)
    }
    result=r.post(url,headers=headers)
    return result