import identifier
import json

ret = identifier.identify('TestImages/eq5.png')
print(ret)
# ret = json.loads(ret)

# if(ret['types'] == identifier.LINEAR):
#     print(ret)
# elif(ret['types'] == identifier.LINEAR2):
#     ret_2 = identifier.identify('eq1.png')
#     print(ret)
#     print(ret_2)
