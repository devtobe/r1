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




