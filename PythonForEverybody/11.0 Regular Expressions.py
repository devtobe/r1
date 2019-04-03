'''
# Regular Expression Quick Guide:
^   begin with
$   end with
.   any characters
\s  whitespace
\S  any non-whitespace character
*   repeats a character zero or more times
*?  repeats a character zero or more times (non-greedy)
+   repeats a character one or more times
+?  repeats a character one or more times (non-greedy)
(   indicates where string extraction is to start
)   indicates where string extraction is to end



# The old way of searching:

handle = open("mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if line.find("From: ") >= 0:
        print(line)



# Compare: The new way of searching: "
# re.search() returns boolean statement

import re
handle = open("mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if re.search("From: ", line):
        print(line)



# The old way of searching something startswith():

handle = open("mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if line.startswith("From: "):
        print(line)


# Compare: The new way of searching something startswith():

handle = open("mbox-short.txt")
for line in handle:
    line = line.rstrip()
    if re.search("^From: ", line):
        print(line)



# Search lines starts with "F..m: " & .. means any characters:

for line in handle:
    line = line.rstrip()
    if re.search("^F..m: ", line):
        print(line)



# Search lines starts with "From: " & .means any characters more than one & @ does not mean anything:

for line in handle:
    line = line.rstrip()
    if re.search("^From: .+@", line):
        print(line)



# "[0-9]+" means more than one digit
# re.findall() extracts data

import re
x = "My 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)
y = re.findall("[AEIOU]+", x)
print(y)



# GREEDY MATCHING: the repeated characters (* and +) push outward in both directions(greedy) to match the largest possible string
# ^F.+: greedy matching
# ^F.+?: do not be greedy



# How to extract email addresses from mbox-short.txt
import re
handle = open("mbox-short.txt")

for line in handle:
    line = line.rstrip()
    if re.search("^From: ", line):
        emails = re.findall("\S+@\S+",line)
        print(emails)


# The above code can also be written to the following:
# The matching part is ^From: (\S+@\S+), but the extracting part is (\S+@\S)

import re
handle = open("mbox-short.txt")

for line in handle:
    line = line.rstrip()
    if re.search("^From: ", line):
        emails = re.findall("^From: (\S+@\S+)", line)
        print(emails)

'''

# How to extract "uct.ac.za" from "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# Three kinds of code to achieve that:

# First:
info = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
index1 = info.find("@")
index2 = info.find(" ", index1)
print(info[index1+1:index2])

# Second (Double split method):
info = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
words = info.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])

# Third (Regular expression):
import re
info = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
host = re.findall("@(\S+)",info) # This line of code can also be: host = re.findall("@([^ ]+)", info)
print(host)


# How to extract all floating numbers following "X-DSPAM-Confidence: " in file "mbox-short.txt"?
# Afterwards, find the largest number in all of these extracted numbers.
import re
file = open("mbox-short.txt")
number_list = list()

for line in file:
    line = line.rstrip()
    string_number = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line) #[0-9.]+ is looking for floating points like 0.8765
    if len(string_number) != 1: continue
    float_number = float(string_number[0])
    number_list.append(float_number)
print("The largest number is " + str(max(number_list)))


# Escape sign \ meaning change the regular expression sign back to normal sign
import re
x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+", x) # if there is no \ before $, then $ will be function as a regux.
print(y)

a = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
b = re.findall("\S+@?\S+", a)
print(b)


a = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
b = re.findall("\S+?@\S+", a)
print(b)
















