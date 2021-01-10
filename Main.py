from Validate import Validate
from CaseInfo import GetCase
from VoteOperationCalculate import VoteCalculate
import sys
import json as js

# access_key=sys.argv[1]
cid=1639369

if __name__ == "__main__":
    case=GetCase(cid).text
    caseinfo=js.loads(case)
    voteBreak=caseinfo['data']['voteBreak']
    voteDelete=caseinfo['data']['voteDelete']
    voteRule=caseinfo['data']['voteRule']
    print(voteBreak,voteDelete,voteRule)
    operation=VoteCalculate(voteBreak,voteDelete,voteRule)
    print(operation)