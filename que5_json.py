import json
def complex_num(object):
    if '_complex_' in object:
        return complex(object['rani'],object['solanki'])
    return object
complex_object=json.loads('{"_complex_":true,"rani":4,"solanki":5}',object_hook=complex_num)
# simple_object=json.loads('{"real":4,"img":3}',object_hook=is_complex_num)
print( "complex_object:",complex_object)
# print("without complex object:",simple_object)
