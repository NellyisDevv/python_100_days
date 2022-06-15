# Print works exactly like console.log in javascript!
from re import A


print("Hello World!")

print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# Printing multiple strings with \n
# Hello world will now print three times inside of a new line!
print("Hello World! \n Hello World! \n Hello World!")

# We can bombine two strings by using the + operator
print("Hello " + "Nelly!")
# You can also add a space between strings like this!
print("Hello" + " " + "Nelly!")

#Input allows you to ask the user for information!
input('What is your name?')
# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?") + "!")

print(input("What is your name?"))
# len() takes a string and tells us how many characters it contains
print(len('Nelly'))
# There are 5 characters in this string!
# We can take this a step forward by asking for an input
# and then giving the length of the users input!
print(len(input("What is your name?")))

# Variables allow you to store information!
name = input("What is your name?")
# You can now refer to the variable "name" whenever you want!
print(name)
# Example!
# We store a string into a variable and then print the variable
person = "Matthew"
print(person)
# Because Python reads from top to bottom person is now "Samuel"
person = "Samuel"
print(person)
# Variables allow you to break things into small pieces!
name = input("What is your name?")
length = len(name)
print(length)

# Fliping variables Exercise
a = input("a: ")
b = input("b: ")
# To flip these variables make a new variable called "c"
c = a 
a = b 
b = c
# Now print the fliped variables
print("a: " + a)
print("b: " + b)

# Rules for naming variables
# Name variables with meaning!
# This ensures you remember what the variable does
# More than one word in python?
# use the _ "underscore" to separate words!
user_name = "My user name!"
# You can use numbers in the name of variables
# You can't use a number as the first letter in variable
# 2length = input("What is your name?") is not valid!
# Do not use the name of functions for variables!
# input = input("What is your name") is not good practice!