'''
friends = ["Sally", "Pam", "Kelly"]
for friend in friends:
    print("Welcome, " + friend + "!")

for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year, " + friend + "!")
'''


# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.


file = open(input("Enter a file name: "))
words_list1 = []
words_list2 = []

for line in file:
    words = line.split()
    words_list1 = words_list1 + words

for word in words_list1:
    if word in words_list2:
        continue
    else:
       words_list2.append(word)

words_list2.sort()

print(words_list2)







