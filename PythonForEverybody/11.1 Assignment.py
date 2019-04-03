# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# The basic outline of this problem is to read the file,
# look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+'
# and then converting the extracted strings to integers and summing up the integers.


import re
handle = open("actualdata.txt")
list_num = list()

for line in handle:
    line = line.rstrip()
    string_num = re.findall("[0-9]+", line)
    if len(string_num) == 0: continue

    for num in string_num:
        int_num = int(num)
        list_num.append(int_num)

print(sum(list_num))