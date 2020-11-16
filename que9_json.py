dict1={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
import json
plce1=open("tes2.json","w")
json.dump(dict1,plce1,indent=4)
plce1.close()
# main dekhna chahta hu shopping list ko json file dekhna.
# for document in dict1:
#     document.write(dict1.[document])
#     print(document)

# kya karedna chahate hai user
