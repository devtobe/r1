import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))



import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
        <user x="13">
            <id>040</id>
            <name>Joe</name>
        </user>
    </users>
</stuff>'''


stuff = ET.fromstring(input)
list_users = stuff.findall("users/user")
print("User count: ", len(list_users))

for item in list_users:
    print("Name", item.find("name").text)
    print("ID", item.find("id").text)
    print("Attribute: ", item.get("x"))