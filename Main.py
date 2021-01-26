from Validate import Validate
from CaseInfo import GetCase
from VoteOperationCalculate import VoteCalculate
from VoteOperation import Vote
from CaseParser import Parse
from GetJudgerInfo import GetInfo
from GetNewCase import GetNew
import sys
import json as js
import requests as r

access_key=None
csrf=None
GiveUpEnable=True
cid=1665870
sessdata='d4f2d79c%2C1625794971%2Ceeebc*11'
cookie=str('_uuid=50680464-FB7B-6B0B-0B2A-24A23558A94804314infoc; buvid3=696DD787-E632-42B6-A6DD-FFFC49B3477A53928infoc; sid=6489cs4o; LIVE_BUVID=AUTO4915841755463172; rpdid=|(J~RYuuYmRR0J\'ul)Ru~llR); Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1584957346; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1585221804; balh_season_ss26953=1; balh_season_ep267800=1; balh_season_ss28137=1; balh_season_ep267801=1; balh_season_26953=1; balh_season_ep267805=1; balh_season_ep267806=1; balh_season_ep267807=1; balh_season_ep267808=1; balh_season_ep317543=1; balh_season_ep317934=1; finger=158939783; balh_season_ss33868=1; balh_season_ep330504=1; balh_season_ep330505=1; balh_season_ep330506=1; balh_season_ep330507=1; balh_season_ep330508=1; balh_season_ep330509=1; balh_season_ep330510=1; blackside_state=1; CURRENT_FNVAL=80; fingerprint3=0873f9cd9e0dc89f381e481910c10d33; bsource=search_google; fingerprint=1a5ad538f5e1768bca7ac0ffd2aec3be; buvid_fp_plain=696DD787-E632-42B6-A6DD-FFFC49B3477A53928infoc; buivd_fp=696DD787-E632-42B6-A6DD-FFFC49B3477A53928infoc; CURRENT_QUALITY=112; balh_server_inner=__custom__; balh_is_closed=; fingerprint_s=973cd062b47155104612cb795635316b; buvid_fp=696DD787-E632-42B6-A6DD-FFFC49B3477A53928infoc; PVID=3; bp_video_offset_44666814=475305553701421211; bp_t_offset_44666814=475159108204736810; DedeUserID=44666814; DedeUserID__ckMd5=588dedeb55a7bd69; SESSDATA=d4f2d79c%2C1625794971%2Ceeebc*11; bili_jct=aa81e4ed2cf94d85b742d5d3ad6fde9a')
session=r.session()



def Main():
    Userinfo=GetInfo(cookie,sessdata)
    print('获取到用户信息，具体如下：')
    print(Userinfo)
    case=GetCase(cid).text
    caseinfo=js.loads(case)
    print(caseinfo)
    printinfo=Parse(case)
    toprint='''
获取到风纪委员案件，具体信息如下：
{}
    '''.format(printinfo)
    print(toprint)
    voteBreak=caseinfo['data']['voteBreak']
    voteDelete=caseinfo['data']['voteDelete']
    voteRule=caseinfo['data']['voteRule']
    operation,operation_print=VoteCalculate(voteBreak,voteDelete,voteRule,GiveUpEnable)
    operation_output='案件{}的投票结果计算为{}，正在进行投票操作……'.format(caseinfo['data']['id'],operation_print)
    print(operation_output)
    # Voteresult=Vote(operation,cid,csrf,sessdata)
    # print(Voteresult)
    print('已完成投票操作！')

if __name__ == "__main__":
    Main()