# Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced,
# the program reads through the dictionary
# using a maximum loop to find the most prolific committer.


file = open(input("Please enter a file name: "))
counts = dict()

for line in file:
    if line.startswith("From "):
        pieces = line.split()
        person = pieces[1]
        counts[person] = counts.get(person, 0) +1

bigcount = 0
for person,count in counts.items():
    if count > bigcount:
        bigperson = person
        bigcount = count

print(bigperson, bigcount)














