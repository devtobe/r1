print("Hello World")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "Tom"
character_age = 50
is_male = True
print("There once was a man named " + character_name + ",")
print("he was " + str(character_age) + " years old. ")

character_name = "Mike"
character_age = 90
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".")

print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool.")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Flamingo"))


print(2.8907)
print(-2.8907)
print(2 + 4.5)
print(2 * 8)
print(2 * 4 + 5)
print(2 * (4 +5))
print(10 % 3)


my_num = -5
print(str(my_num) + " is my favourite number.")
print(abs(my_num))
print(pow(3,2))
print(max(4,6))
print(min(6,2))
print(round(4.6))

from math import *
print(floor(4.6))
print(ceil(7.8))
print(sqrt(36))

#user_name = input("Enter your name: ")
#user_age = input("Enter your age: ")
#print("Hello " + user_name + "!")
#print("You are " + user_age + ".")

#   How to build a calculator?
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = int(num1) + int(num2)
#print(result)
#   int() is looking for a whole number

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)
#   float() is looking for numbers with decimal points

#   How to create a maglib game?
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)


#   lIST IN PYTHON
friends1 = ["Kevin", "Kelly", "Karen", "Kathy", "Kate"]
print(friends1[0])
print(friends1[-2])
print(friends1[1:])
print(friends1[1:4])

friends1[1] = "Mike"
print(friends1[1])

lucky_numbers = [74, 6, 27, 2, 25, 18]
friends2 = ["James", "Jeff", "Jeff", "Jeff", "Ivy", "Pam", "Flora", "Joe"]

#friends2.extend(lucky_numbers)
#print(friends2)

friends2.append("Toby")
print(friends2)

friends2.insert(1, "Peter")
print(friends2)

friends2.remove("Joe")
print(friends2)

friends2.pop()
print(friends2)

print(friends2.index("Pam"))

print(friends2.count("Jeff"))

friends2.sort()
print(friends2)

friends2.clear()
print(friends2)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends3 = friends1.copy()
print(friends3)



#   Tuples in Python: Tuple is immutable, which means it cannot be changed.
coordinates = (4, 5, 9, 0)
print(coordinates[1])



#   How to Create Functions in Python?
def say_hi(hello_name, age):
    print("Hello " + hello_name + ", you are " + str(age) + ".")

say_hi("Steve", 30)


def cube(base_num):
    return base_num * base_num * base_num

print(cube(5))


#   IF STATEMENT
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a male but not tall.")
elif not(is_male) and is_tall:
    print("You are tall but not male.")
else:
    print("You are neither tall nor male.")



def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,10,1))
# comparisons: == !=


#   BUILD A CALCULATOR
#numm1 = float(input("Enter first number: "))
#operator = input("Enter operator: ")
#numm2 = float(input("Enter second number: "))

#if operator == "+":
    #print(numm1 + numm2)
#elif operator == "-":
    #print(numm1 - numm2)
#elif operator == "*":
    #print(numm1 * numm2)
#elif operator == "/":
    #print(numm1 / numm2)
#else:
    #print("invalid operation")



#   WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


#   BASIC GUESS GAME
#secret_word = "giraffe"
#guess = ""

#while guess != secret_word:
#    guess = input("Enter guess: ")

#print("You win!")


#   More COMPLEX GUESSING GAME
#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guess = False

#while guess != secret_word and not(out_of_guess):
    #if guess_count < guess_limit:
        #guess = input("Enter guess: ")
        #guess_count += 1
    #else:
        #out_of_guess = True

#if out_of_guess:
    #print("Out of guesses. You lose!")
#else:
    #print("You win!")


#   FOR LOOP
for letter in " Giraffe Academy ":
    print(letter)

friends_name = ["Jim", "Karen", "Kelly"]
for friend_name in friends_name:
    print(friend_name)

for index in range(10):
    print(index)

for index in range(3,10):
    print(index)

for index in range(len(friends_name)):
    print(friends_name[index])

for index in range(5):
    if index == 0:
        print("first interation")
    else:
        print("not first")


#   Exponent Function
print(2**3)

#base_num = input("Enter base number: ")
#power_num = input("Enter power number: ")

#def raise_to_power(base_num, power_num):
    #result = 1
    #for index in range(int(power_num)):
        #result = result * int(base_num)
    #return result

#print(raise_to_power(base_num,power_num))



#   TWO DIMENTIONAL LIST
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(num_grid[2][0])


for row in num_grid:
    for col in row:
        print(col)



#   BUILD A TRANSLATOR
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
}

print(month_conversions["Aug"])
print(month_conversions.get("Feb"))
print(month_conversions.get("luv"))
print(month_conversions.get("luv", "not a valid value"))

'''
   BUILD GIRAFFE TRANSLATOR
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
'''



'''
#   Catching Errors -- TRY EXCEPT

try:
    number = int(input('Enter a number: '))
    print(number)
except ValueError:
    print("invalid input")
'''

#   READ EXTERNAL FILE
employee_file = open("employee.txt", "r")

print(employee_file.readable())

print(employee_file.readline())

print(employee_file.read())

print(employee_file.readlines())

employee_file.close()


#   WRITE / APPEND TO EXTERNAL FILE
employ_file = open("employee.txt", "a")

employ_file.write("\nToby - Human Resources")

employee_file.close()




employ_file = open("employee.txt", "w")

employ_file.write("Toby - Human Resources")

employee_file.close()




employ_file = open("employee1.txt", "w")

employ_file.write("Toby - Human Resources")

employee_file.close()



#   MODULES
import useful_tools

print(useful_tools.roll_dice(12))


#   Class & Objects
from Student import Student

student1 = Student("Jim", "Business", 3.1)
student2 = Student("Pam", "Art", 2.5)

print(student1.name)
print(student2.gpa)

'''
#   BUILD A MULTIPLE CHOICE QUIZ
from Questions import Question

question_prompts = [
    "What color are apples? \n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You get " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)
'''


from Student import Student

student5 = Student("Oscar", "accounting", 3.4)
student6 = Student("Tracy", "Chemistry", 3.6)

print(student5.on_honor_roll())


#   Inheritance
from Chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()
my_chef.make_special_dish()

my_ChineseChef = ChineseChef()
my_ChineseChef.make_special_dish()


















