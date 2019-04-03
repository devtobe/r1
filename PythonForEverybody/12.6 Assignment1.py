'''
* EXERCISE:
Scraping Numbers from HTML using BeautifulSoup
In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the sum of the numbers in the file.

* IMPORTANT:
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
'''


from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_handle = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_203148.html", context=ctx).read()
soup = BeautifulSoup(file_handle, "html.parser")
lines = soup("span")

sum = 0

for line in lines:
    str_nums = line.contents[0]
    int_nums = str_nums.split()

    for num in int_nums:
        sum = sum + int(num)

print(sum)
