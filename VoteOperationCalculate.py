def VoteCalculate(BreakVote,DeleleVote,RuleVote):
    approve=BreakVote+DeleleVote
    deny=RuleVote
    proportion=approve/deny
    result=None
    if(proportion>=0.7):
        if DeleleVote>=BreakVote:
            result='Delete'
        else:
            result='Break'
    elif(proportion<=0.3/0.7):
        result="Rule"
    return result