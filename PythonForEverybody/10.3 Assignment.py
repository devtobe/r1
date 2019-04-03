# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file = open(input("Please enter a file name: "))
list_hours = []
dic_hours = dict()

for line in file:
    if line.startswith("From "):
        pieces = line.split(":")
        hours = pieces[0].split()
        list_hours.append(hours[-1])

for hour in list_hours:
    dic_hours[hour] = dic_hours.get(hour, 0) +1

for key, value in sorted(dic_hours.items()):
    print(key, value)

