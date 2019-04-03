# Write a program that prompts for a file name
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

file = input("Enter a file name: ")
content = open(file)

for line in content:
    print(line.rstrip().upper())