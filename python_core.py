#Simple Calculator 
#Take two numbers as input and output their sum 
#x = int(input("Enter first number "))
#y = int(input("What number do you want to add? "))
x, y = 4, 7
result = x + y
print(str(x) + " + " + str(y) + " = " + str(result))

#Chaining Multiple Conditions
print("MULTIPLE CONDITIONS")
print("UNIVERSITY DISCOUNT TRACKER")
#The university gives students discounts on tuition fees depending on their performance:
#90-100 => 50%
#80-89 => 30%
#70-79 => 10%
#0-69 => 0%
#Write a program that will take the scores from the first and second semesters, then calculate the average score, and output the discount, depending on the score.
print("Let's track your discount amount based on your previous grades at university.")
#score1 = int(input("what was your grade the first semester? "))
#score2 = int(input("What was your grade the second semester? "))
score1, score2 = 34, 59

score = (score1 + score2) / 2

if score <= 69:
    print("Sorry your discount is 0%.")
if score >= 70 and score <= 79:
    print("Good job, you are entitled to a 10% discount.")
if score >= 80 and score <= 89:
    print("Great job, you are entitled to a 30% discount.")
if score >= 90 and score <= 100:
    print("Congratulations. Your hard work has earned you 50% discount of your fees. ")

#FizzBuzz
print("FIZZBUZZ")
print("Output all numbers unless they are a multiple of 3 or 5.  We'll print FizzBuzz in place of 3 & 5.")
#It takes an input n and outputs the numbers from 1 to n.
#For each multiple of 3, print "Fizz" instead of the number.
#For each multiple of 5, prints "Buzz" instead of the number.
#For numbers which are multiples of both 3 and 5, output "FizzBuzz".

#You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.
#n = int(input())
n = 16
for x in range(1, n, 2): #use range with skip of 2 to only check odd numbers 
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

#Celsius to Fahrenheit 
print("CELSIUS TO FAHRENHEIT CONVERTER")
#Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.
#The following equation is used to calculate the Fahrenheit value: 9/5 * celsius + 32
#celsius = int(input("What are the degrees in celsius? "))
celsius = 33
def conv(c):
    #your code goes here
    temp = ((9/5) * (celsius)) + 32
    return temp

fahrenheit = conv(celsius)
print(str(celsius) + " degrees celsius is equal to " + str(fahrenheit) + " degrees in fahrenheit")

#Book Titles 
#You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
#The code is equal to the first letter of the book, followed by the number of characters in the title.
#For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

#You are provided a books.txt file, which includes the book titles, each one written on a separate line.
#Read the title one by one and output the code for each book on a separate line.

#file = open("/usercode/files/books.txt", "r") #if you add a text file you used this
file = """The Mad Hatter
The Red Book
Alice Wonderland
Some Book
Another Book
The Girl in the Box
Last Book"""
#your code goes here
#for i in file.read().splitlines(): # uncomment this to read a txt file 
for i in file.splitlines():    
    type = str(len(i))
    for x in i:
        
            print(x+(type))
            break        


#file.close() #close the text file after reading

#Longest Word 
# Given a text as input, find and output the longest word.
#txt = input()
txt = "Supercalifragilisticexpialidocious is the longest word I know"
longest_word = max(txt.split(), key=len)
print(longest_word)

#Fibonacci Sequence
#Each number in the sequence is the sum of the two numbers that precede it.
#For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.
#Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).
#num = int(input("What is the range you want to check?"))
num = 10
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(num):
    print(fibonacci(n))

#Juice Maker 
#You are given a Juice class, which has name and capacity properties.
#You need to complete the code to enable and adding of two Juice objects, resulting in a new Juice object with the combined capacity and names of the two juices being added.
#For example, if you add an Orange juice with 1.0 capacity and an Apple juice with 2.5 capacity, the resulting juice should have:
#name: Orange&Apple capacity: 3.5
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)
result =( a.name + "&" + b.name )+ " " + "(" + ( str(a.capacity + b.capacity )) + "L" + ")"
print(result)
#Phone Validator using Regex
#You are given a number input, and need to check if it is a valid phone number.
#A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
#Output "Valid" if the number is valid and "Invalid", if it is not.
from csv import excel_tab
import re

#phone = input("Enter an 8 digit number starting with 1, 8 or 9= ")
phone = ("18937656", "67829", "18926737", "93928473", "48787987") #list of phone numbers
regex =r"^[189][0-9]{7}$"
for r in phone:
    match = re.match(regex, r)
    if match:
        print("Valid")
    else:
        print("Invalid")

#Phone validator without list 
import re
#your code goes here
#phone = input()
phone="18762564"
regex =r"^[189][0-9]{7}$"
match = re.match(regex, phone)
if match:
    print("Valid")
else:
    print("Invalid")


#Zen of Python
#import this #way to print principles of programming

#Function Arguments 
#*args to pass an arbitrary number of arguments to that function.  The argument is accessible as the tuple args. 
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

#Default Values 
def function(x, y, food="spam"):
    print(food)
function(1, 2) #will output 'spam' as default since no food defined
function(3, 4, "egg") #prints 'egg'

#Keyword Arguments - 
# **kwargs - handle named argument that are not defined in advance 
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
my_func(2, 3, 4, 5, 6, a=7, b=8)

#Tuple Unpacking
#Allows you to assign each item in an iterable to a variable.
numbers = (1, 2, 3)
a, b, c = numbers 
print(a)
print(b, c)

#A variable that is prefaced with asterisk takes all values from the iterable that are left over from the other variables
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

#Ternary Operator 
#Provide if statement functionality with less code - don't overuse
a = 7 
b = 1 if a >= 5 else 42
print(b)

status = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

#Else Statements 
for i in range(10):
    if i == 999: 
        break
else:
        print("Unbroken 1")
for i in range(10):
    if i == 5:
        print("For loop finished abnormally")
        break
else:
    print("Unbroken 2")

#Try/Except Statements
print("Calculate: 1/2")
try:
    print(1/2)
except ZeroDivisionError:
    print("Error: Can't divide by zero")
else:
    print("Division succeeded")
print("Calculate: 1/0")
try:
    print(1/0)
except ZeroDivisionError:
    print("Error: Can't divide by zero")
else:
    print("Division succeeded")

#Another example
try:
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError:
    print("Error: Type Error")
else:
    print("Success")

#Concatenate w/ Args
def concatenate(*args, sep = "-"):
    return sep.join(args)

print(concatenate("I", "love", "Python", "!", sep= "-"))
