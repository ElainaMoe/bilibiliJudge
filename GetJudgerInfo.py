import requests as r
import json as js

url='http://api.bilibili.com/x/credit/jury/jury'



def GetInfo(SESSDATA):
    test='SESSDATA={}'.format(SESSDATA)
    headers={
        'cookie': test,
    }
    info=r.get(url,headers=headers)
    info_loads=js.loads(info.text)
    status={
        1: '具有资格',
        2: '资格失效'
    }
    parsed=str({
        '用户名': info_loads['data']['uname'][0]+ ('*' * int(len(info_loads['data']['uname'])-2)) +info_loads['data']['uname'][len(info_loads['data']['uname'])-1:],
        '已裁决案件数': info_loads['data']['caseTotal'],
        '资格状态': status[info_loads['data']['status']],
        '剩余资格天数': info_loads['data']['restDays'],
        '裁决准确率': str(info_loads['data']['rightRadio'])+'%'
    })
    return info_loads,parsed