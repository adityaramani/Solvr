import getEquation as ge
import json

ret = ge.getLhsRhs('eq3.png')
ret = json.loads(ret)
if(ret['types'] == ge.LINEAR):
    print(ret)
elif(ret['types'] == ge.LINEAR2):
    ret_2 = ge.getLhsRhs('eq1.png')
    print(ret)
    print(ret_2)
