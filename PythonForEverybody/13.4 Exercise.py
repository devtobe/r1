# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL,
# read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.

import urllib.request, urllib.error, urllib.parse
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_file = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_203150.xml", context=ctx).read()
tree = ET.fromstring(url_file)
data = tree.findall("comments/comment")

sum = 0
for item in data:
    num = int(item.find("count").text)
    sum = sum + num
print(sum)
