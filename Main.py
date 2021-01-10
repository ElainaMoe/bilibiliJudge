from Validate import Validate
from CaseInfo import GetCase
import sys

access_key=sys.argv[1]
cid=1639369

if __name__ == "__main__":
    # verify=Validate(access_key)
    # print(verify.text)
    case=GetCase(cid)
