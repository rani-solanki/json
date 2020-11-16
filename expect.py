import json
filename= 'test.txt'
dict1={ }
fields=["name","destignation","age","sa"]
with open (filename) as fh:
    j=1
    none="rani"
    for line in fh:
        description=list(line.strip().split(none))
        print(description)
        sno='emp'+str(j)
        i=0
        dict2={}
        while(i<len(fields)):
            dict2[fields[i]]=description[i]
            i=i+1
        dict1[sno]=dict2
        j=j+1
out_file=open("test2.json","w")
json.dump(dict1,out_file,indent=4)
out_file.close()
