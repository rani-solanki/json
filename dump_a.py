import json
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}   
# the json file where the output must be stored 
out_file = open("myfile.json", "w") 
   
json.dump(dict1, out_file, indent = 6)
print(type(dict1)) 
   
out_file.close() 

# # use of json.dumps
# import json
# a={'lalalala': 3}
# # json.dumps() is canvert python object to json string.
# mystring = json.dumps(a)
# print(mystring)
# print(type(mystring))


