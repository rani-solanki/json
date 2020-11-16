book={}
book['tom'] = {
    'name' : 'tom',
    'addres':'1 red street,ny',
    'phone' : 46876438723
}
book[ 'bob' ] = {
    'name' : 'bob',
    'addres' : '1 green street,ny',
    'phone' : 7554287394
}
import json
j=json.dumps(book)
# print(type(j))
book=json.loads(j)
print(book)
# print(type(book))
for key1 in book:
    for key2 in book[key1]: 
        print(key2)

# write data in text file
with open("saral.txt","w") as f:
    f.write(j)





