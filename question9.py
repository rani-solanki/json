plce=open("test.txt","r")
plce.read()
print(plce)
import json
plce1=open("test2.json","w")
json.dump(plce1,indent=4)
plce1.close( )
# Python program to convert text 
# file to JSON 
  
  
# import json 
# filename = 'test.txt'
# dict1 = { }
# # creating dictionary 
# plce=open("filename","r")
# for line in plce:
#     k, v = line.strip().split('=')
#     answer[k.strip()] = v.strip()
# plce.close()
# out_file = open("test2.json", "w") 
# json.dump(dict1, out_file, indent = 4, sort_keys = False) 
# out_file.close()
# d = {}
# with open("test.txt") as f:
#     for line in f:
#         print(line)
#         (key, val) = line.split()
#            print(key,val)
#          d[] = val
#      print (d)