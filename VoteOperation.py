import requests as r
import json as js
voteurl='http://api.bilibili.com/x/credit/jury/vote'

voteaction={
    'Break': 1,
    'Rule': 2,
    "GiveUp": 3,
    'Delete': 4
}

def Vote(opreation,cid,csrf,sessdata):
    headers={
        'cookie': 'SESSDATA={}'.format(sessdata),
        'Host': 'api.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }
    params={
        'cid': cid,
        'vote': voteaction[opreation],
        'attr': 0,
        'csrf': csrf
    }
    VoteReturn=r.post(voteurl,params=params,headers=headers).text
    VoteResult=js.dumps(VoteReturn)
    return VoteResult