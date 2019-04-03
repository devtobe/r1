# Using urllib in Python
# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file


# Print the file
import urllib.request, urllib.parse, urllib.error
file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in file_handle:
    print(line.decode().rstrip())

print()

# count the word in the file
import urllib.request, urllib.parse, urllib.error
file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in file_handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

print(counts)
print()


# Read HTML web page
import urllib.request, urllib.parse, urllib.error
file2_handle = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")

for line2 in file2_handle:
    print(line2.decode().strip())






