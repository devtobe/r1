# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

'''
file = open(input("Please enter a file name: "))
count = 0
value = 0

for line in file:
    if "X-DSPAM-Confidence" in line:
        index = line.find("0")
        value = value + float(line[index:])
        count = count +1

average = value / count

print("Average spam confidence: " + str(average))

'''

fruit = "Banana"
fruit[0] = "b"
print(fruit)