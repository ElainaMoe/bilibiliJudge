import requests as r
import json as js

url='http://api.bilibili.com/x/credit/jury/jury'

def GetInfo(SESSDATA):
    cookie='SESSDATA={}'.format(SESSDATA)
    headers={
        'cookie': cookie,
        'Host': 'api.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }
    info=r.get(url,headers=headers)
    info_loads=js.loads(info.text)
    status={
        1: '具有资格',
        2: '资格失效'
    }
    username='***'
    parsed=str({
        '用户名': username,
        '已裁决案件数': info_loads['data']['caseTotal'],
        '资格状态': status[info_loads['data']['status']],
        '剩余资格天数': info_loads['data']['restDays'],
        '裁决准确率': str(info_loads['data']['rightRadio'])+'%'
    })
    return info_loads,parsed
