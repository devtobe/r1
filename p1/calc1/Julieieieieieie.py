'''
Created on Dec 30, 2017

@author: Julie
'''
#Variables Naming rules: 
#Variables can only contain letters, numbers, and underscores. 
#Variable names can start with a letter or an underscore, but can not start with a number.
#Spaces are not allowed in variable names, so we use underscores instead of spaces.
#NO Python keywords.
#Variable names should be descriptive, without being too long. 
#Be careful with letters l O and numbers 1 and 0.

#Values need to come with single/double quotation marks. 
print('Hi Python')

message = "Julie is learning Python"
print(message)

message = "It is very hard to get started"
print(message)

#A method can be indicated by "variable_name.action()"
first_name = "julie"
print(first_name.title())
print(first_name.upper())
print(first_name.lower())

first_name = "julie"
last_name = "huang"
full_name = first_name + " " + last_name
print(full_name.title())

first_name = "julie"
last_name = "huang"
full_name = first_name + " " + last_name
message = full_name.title() + " " + "is the world's fastest programming learner."
print(message)

print("julie huang \tis the world's \nfastest programming learner.")

#The most common whitespace characters are spaces, tabs, and newlines.
name = "   Julie   "  
print("_" +name + "_")
print("_" + name.lstrip() + "_")
print("_" + name.rstrip() + "_")
print("_" + name.strip() + "_")

quote = "God said 'let there be light', and there was light."
print(quote.title())
print(quote.upper())
print(quote.lower())

quote1 = "God said 'let there be light.'"
quote2 = "God said 'do not kill.'"
quote = quote1 + " and " + quote2
print(quote.title())

name = "god"
message = name.title() + " " + "is my creator."
print(message)

name = "   God   "
print(name.lstrip() + " " + "is my creator.")
print(name.rstrip() + " " + "is my creator.")
print(name.strip() + " " + "is my creator.")

#Quotation marks won't be needed for integers operations. 
print(3**2+4*2-1/0.5)

my_order = 3**2+4*2-1/0.5
print(my_order)

my_order = 3**2+4*(2-1)/0.5
print(my_order)

print(0.2+0.1)
print(0.3+0.6)
print(0.4+0.8)
print(3/2)

print()

dogs = ['australian cattle dog','border collie','labrador retriever']
dog = dogs[0]
#The number in square brackets is called the index of the number. 
print(dog.title())
dog = dogs[1]
print(dog.title())
dog = dogs[2]
print(dog.title())

#To get the last item in a list, no matter how long the list is, you can use an index of -1.
dogs = ['australian cattle dog','border collie','labrador retriever','golden retriever','australian shepherd']
dog = dogs[-1]
print("\n" + dog.title())
#This syntax also works for the second to last item, the third to last, and so forth.
dog = dogs[-2]
print(dog.title())

first_list = ['java','javascript','python','c++']
language = first_list[-2]
print(language.title() + " " + "is an interesting computing language.")

print()

dogs = ['border collie','golden retriever','australian shepherd','labrador retriever','australian cattle dog']
for dog in dogs:
    print(dog)
    print(dog + "s" + " " +"is very cute.\n")

print()

computer_languages = ['java', 'c++', 'python','javascript']
for computer_language in computer_languages:
    print("I find learning" + " " + computer_language.title() + " " + "is very interesting.\n")
print('But among all, I find Python is my favorite.')

print()

#The enumerate() function tracks the index of each item for you, as it loops through the list.
dogs = ('border collie','labrador retriever','australian shepherd','australian cattle dog')
for index, dog in enumerate(dogs):
    print('Place:' + str(index+1) + ' Dog:' + dog.title())

print()

kids = ('Will','Morgan','Shirley','Benjamin')
for kid in kids:
    print('I love my kid' + " " + kid + " " + "very much.\n")

print()

kids = ('Will','Morgan','Shirley','Benjamin')
for index, kid in enumerate(kids):
    print("My " + str(index+1) + " kid is " + kid + ".\n")

basketball_players = ('JeremyL','YaoM','StephenC','MichaelJ')
for index, basketball_player in enumerate(basketball_players):
    print(basketball_player + ' ranks ' + str(index+1) + '.\n')
    print(basketball_players.index('YaoM'))

#You can test whether an item is in a list using the "in" keyword. 
    print("StephenC" in basketball_players)
    print("ChuanH" in basketball_players)

print()

dogs = ['shiba','labrador retriver','collie']
dogs.append('australian cattle')
for dog in dogs:
    print(dog.title() + "s are very cute.")
#We can also insert items anywhere we want in a list, using the insert() function. 
#We specify the position we want the item to have, and everything from that point on is shifted one position to the right.
dogs.insert(1,'poodle')
for dog in dogs:
    print('\n' + dog.title() + "s are very cute.")

print()
# Create an empty list to hold our users.
usernames = []
usernames.append('shirley')
usernames.append('benson')
usernames.append('emma')
usernames.append('julie')
for username in usernames:
    print('Welcome ' + username.title() + '!')
# Recognize our first user, and welcome our newest user.
print('Thank you for being our first user, ' + usernames[0].title() + '!')
print('Thank you for being our newest user, ' + usernames[-1].title() + '!')

print()

# Put students in alphabetical order.
usernames.sort()
print("Our usernames are in alphabetical order:")
for username in usernames:
    print(username.title())
usernames.sort(reverse = True)
print("Our usernames are in reverse alphabetical order:")
for username in usernames:
    print(username.title())
print()

usernames = ['julie','emma','mimi','aaron','benson']
# Whenever you consider sorting a list, keep in mind that you can not recover the original order.
# If you want to display a list in sorted order, but preserve the original order, you can use the sorted() function.
print('Here is the list in alphabetical order:')
for username in sorted(usernames):
    print(username.title())
print('\nHere is the list in reverse alphabetical order:')
for username in sorted(usernames, reverse=True):
    print(username.title())
print('\nHere is the list in original order:')
for username in usernames: 
    print(username.title())
#There is one more order we can use, and that is the reverse of the original order of the list. The reverse() function gives us this order.
usernames.reverse()
print(usernames)
#Reverse is permanent, although you could follow up with another call to reverse() and get back the original order of the list.

print()

list_number = [3,2,1,4]
list_number.sort()
print(list_number)

print()
list_number =[3,2,1,4]
print(sorted(list_number))
print(list_number)

print()

list_number = [3,2,1,4]
list_number.reverse()
print(list_number)

#You can find the length of a list using the len() function.
usernames =['aaron','holms','joy','enson']
print(len(usernames))

print()
#Exercise: 
careers = ['programmer', 'truck driver','attorney', 'president']
#Use the list.index() function to find the index of one career in your list.
print(careers.index("attorney"))
print(careers[-1].title())
#Use the in function to show that this career is in your list.
print('teacher' in careers)
print('president' in careers)
careers.append('dancer')
print(careers)
#Use the insert() function to add a new career at the beginning of the list.
careers.insert(0, 'artist')
print(careers)
#Use a loop to show all the careers in your list.
for career in careers:
    print('How much will a ' + career + ' earn normally?')
#Create the list you ended up with in Working List, but this time start your file with an empty list and fill it up using append() statements.
working_list = []
working_list.append('doctor')
working_list.append('cook')
working_list.append('pastor')
working_list.append('lawyer')
print(working_list)
print('The first career in the job list is ' + working_list[0].title() + '.')
print('The last career in the job list is ' + working_list[-1].title() + '.')
print()

#Print the list in its original order.
for job in working_list:
    print(job.title())
#Print the list in alphabetical order.
print()
for job in sorted(working_list):
    print(job.title())
#Print the list in reverse alphabetical order.
print()
for job in sorted(working_list, reverse = True):
    print(job.title())
#Print the list in its original order.
print()
working_list = ['doctor','cook','pastor','lawyer']
for job in working_list:
    print(job.title())
#Print the list in the reverse order from what it started.
print()
working_list.reverse()
for job in working_list:
    print(job.title())
#Print the list in its original order.
print()
working_list = ['doctor','cook','pastor','lawyer']
for job in working_list:
    print(job.title())
#Permanently sort the list in alphabetical order, and then print it out.
print()
working_list.sort()
for job in working_list:
    print(job.title())
#Permanently sort the list in reverse alphabetical order, and then print it out.
print()
working_list.sort(reverse=True)
for job in working_list:
    print(job.title())
