# use of dump function
list=  {"Name":"Ram", "class":"IV","Age":9 }
# open the json file
list1=open("lod.json", "w")
import json
# dump in to json data file
list1=json.dump(list,list1,indent=4)
# out put should come in json object
print(list1)

# #  use of dumps function 
# import json
# x =  { "name":"John", "age":30, "city":"New York"}
# # pass to json file
# a=open("lod.json","w")
# # change json object in to string 
# y = json.dumps(x,indent=4)
# # in string output
# print(y)

# #  use of loads in json
# file='{ "key_1": 1, "key_2": "foo", "Key_3": "null" }'
# # print(type(file))
# import json
# li=json.loads(file)
# print(li)

# # use of load in json
# import json
# list=open("lod.json","r")
# li=json.load(list)
# print(li)