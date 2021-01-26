voteaction={
    'Break': '封禁',
    'Rule': '合规',
    "GiveUp": '放弃',
    'Delete': '删除'
}

def VoteCalculate(BreakVote,DeleleVote,RuleVote,GiveUpEnable):
    approve=BreakVote+DeleleVote
    deny=RuleVote
    try:
        proportion=approve/deny
    except ZeroDivisionError:
        proportion=1
    result=None
    if(proportion>=0.7):
        if DeleleVote>=BreakVote:
            result='Delete'
        else:
            result='Break'
    elif(proportion<=0.3/0.7):
        result="Rule"
    else:
        if(GiveUpEnable):
            result='GiveUp'
        else: 
            result="CannotJudge"
    return result,voteaction[result]