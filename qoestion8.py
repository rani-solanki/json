import json
a=["name","disigner","age","salary"]
b=["neelam","dovelopers","25","25000"]
sa=dict(zip(a,b))
# sl=dict(sa)
# print(sa)
dict1=json.dumps(sa,indent=4)
print(dict1)
# print("emp1",":",sa)
x=["komal","trainer","24","20,000"]
ml=dict(zip(a,x))
dict2=json.dumps(ml,indent=4)
print(dict2)
# print("emp2",":",ml)
y=["anurada","HR","27","40,000"]
kl=dict(zip(a,y))
dict3=json.dumps(kl,indent=4)
print(dict3)
# print("emp3",":",kl)
z=["abhishek","manager","29","63000"]
jl=dict(zip(a,z))
dict4=json.dumps(jl,indent=4)
print(dict4)
# print("emp4",":",jl)
