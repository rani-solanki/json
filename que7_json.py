import json
pl="test.txt"
dict1=[]
dict2=[ ]
with open(pl) as fh:
    for line in fh:
        sa=(line.strip().split())
        dict1.append(sa)
print(dict1)
# for key,value in dict1.items():
#     fg=dict(zip(key,value))
# print(fg)



