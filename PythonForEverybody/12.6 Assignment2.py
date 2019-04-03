# EXERCISE: In this assignment you will write a Python program
# that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input("Enter count: "))
position = int(input("Enter position: "))
link = input("Enter url: ")
repetition = 0

while repetition < count:

    file_handle = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(file_handle,"html.parser")
    tags = soup("a")

    tag = tags[position -1]
    link = tag.get("href", None)

    repetition = repetition + 1

print(tag.contents[0])

