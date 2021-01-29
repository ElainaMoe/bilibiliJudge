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
import time

try:
    csrf=sys.argv[1]
    sessdata=sys.argv[2]
    if(csrf=='' or sessdata==''):
        print('必要变量未设置！程序即将退出！')
        sys.exit()
except:
    print('缺少必要变量！程序即将推出！')
    sys.exit()

try:
    GiveUpEnable=sys.argv[3]
    if GiveUpEnable=='False':
        GiveUpEnable=False
except:
    GiveUpEnable=True

try:
    delay=sys.argv[4]
except:
    delay=300

config={
    '放弃': GiveUpEnable,
    '无法判断等待时间': delay
}
print(config)
ApplyResult=None
cannotJudge=False


def GetAndCal(cid):
    case=GetCase(cid).text
    caseinfo=js.loads(case)
    printinfo=Parse(case)
    toprint='''
获取到风纪委员案件，具体信息如下：
{}
    '''.format(printinfo)
    print(toprint)
    voteBreak=caseinfo['data']['voteBreak']
    voteDelete=caseinfo['data']['voteDelete']
    voteRule=caseinfo['data']['voteRule']
    return voteBreak,voteDelete,voteRule,caseinfo


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
    while True:
        print('正在进行下一案件的获取……')
        cid=GetNew(csrf,sessdata)
        if(cid):
            print('今天案件已经审核满或没有需要仲裁的案件了，明天我们再继续吧~')
            sys.exit()
        voteBreak,voteDelete,voteRule,caseinfo=GetAndCal(cid)
        operation,operation_print=VoteCalculate(voteBreak,voteDelete,voteRule,GiveUpEnable)
        while True:
            if(operation=='CannotJudge'):
                print('目前案件{}的投票数量不足以判定操作，将在{}秒钟后重试！'.format(caseinfo['data']['id'],delay))
                global cannotJudge
                cannotJudge=True
                time.sleep(delay)
                GetAndCal(cid)
            else:
                cannotJudge=False
                break
        operation_output='案件{}的投票结果计算为{}，正在进行投票操作……'.format(caseinfo['data']['id'],operation_print)
        print(operation_output)
        Vote(operation,cid,csrf,sessdata)
        print('已完成投票操作！')
    

if __name__ == "__main__":
    Main()
