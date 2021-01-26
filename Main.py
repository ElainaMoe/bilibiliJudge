from CaseInfo import GetCase
from VoteOperationCalculate import VoteCalculate
from VoteOperation import Vote
from CaseParser import Parse
from GetJudgerInfo import GetInfo
from GetNewCase import GetNew
from JudgementApply import Apply
import sys
import json as js
import requests as r

csrf=sys.argv[1]
GiveUpEnable=True
cid=1665870
sessdata=sys.argv[2]
ApplyResult=None

def Main():
    Userinfo,UserinfoParsed=GetInfo(sessdata)
    print('获取到用户信息，具体如下：')
    print(UserinfoParsed)
    if(Userinfo['data']['status']==2):
        print('检测到未具有风纪委员资格，正在尝试申请……')
        global ApplyResult
        ApplyResult,ApplyMsg=Apply(sessdata,csrf)
    if(ApplyResult):
        print('风纪委员资格申请成功，正在执行脚本操作……')
    elif(not ApplyResult):
        print('申请风纪委员资格失败，{}，脚本即将退出！'.format(ApplyMsg))
        sys.exit()
    cid=GetNew(csrf)
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
    Voteresult=Vote(operation,cid,csrf,sessdata)
    print(Voteresult)
    print('已完成投票操作！')

if __name__ == "__main__":
    Main()