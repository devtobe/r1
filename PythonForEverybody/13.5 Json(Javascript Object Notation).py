# JSON represents data as nested "lists" and "dictionaries"



# return a dictionary. the dictionary has dictionaries in it.
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print(type(info))
print("Name: ", info["name"])
print("Phone Number: ", info["phone"]["number"])
print("Hide: ", info["email"]["hide"])
print()






# return a LIST. the list has dictionary in it.
import json

input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    } , 
    {   "id" : "009",
        "x"  : "7",  
        "name" : "Hon"
    }
]'''

content = json.loads(input)
print(type(content))

print("Counts: ", len(content))

for item in content:
    print("name: ", item["name"])
    print("id: ", item["id"])
    print("Attribute: ", item["x"])