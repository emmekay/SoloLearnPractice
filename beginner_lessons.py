#Exponentiation
#Write program to calculate the amount that will result from doubling 
from ast import arg


result = 0.01*(2**30)
print(result)

#Simple Operations 
#write program to calculate how many seconds in 30 days.
second = 1
minute = 60 * second
hour = 60 * minute 
day = 24 * hour 
month = 30 * day  
print("TIME CONVERSION")
print("How many seconds in a month?")
print("There are " + str(month) + " seconds in a month, if the month has 30 days.")

#Flight Time
#Calculate the flight time. You are flying from LA to Sydney, covering a distance of 7425 miles, the plane flies at an average speed of 550 miles an hour.

#Calculate and output the total flight time in hours.
print("FLIGHT TIME")
flight_hours = 7425/550
print("A plane flies 550 miles an hour over the 7425 miles it takes to travel from LA to Sydney. \n" + "So it will take " + str(flight_hours) + " hours for this trip.") 

#You need to make a program for a leaderboard.
#Strings & New Lines 
# The program needs to output the numbers 1 to 8, each on a separate line, followed by a dot: 1. 2. etc.
print("STRINGS & NEWLINES")
print("Use three quotes or new line to separate print output." )
print("""1.
2.  
3.
4.
5.""")
print("6.\n7.\n8.\n")

#Tip Calculator
#Take bill amount as input and output 20% tip as a float 
print("20% TIP CALCULATOR")
bill = float(input("How much is the bill?")) #Take input as float to accept numbers that aren't whole numbers
#bill = 10.24
tip = round(bill * .2, 2) #The round function is used to round answer up to two decimal points.  The comma then 2 denote the 2 decimals 
print("Please tip your wait staff " + str(tip) + " dollars for good service.") #must convert tip to str in order to print final string 

#BMI
#Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.
#BMI = weight / height²
# Underweight = less than 18.5
#Normal = more or equal to 18.5 and less than 25
#Overweight = more or equal to 25 and less than 30
#Obesity = 30 or more
print("BMI CALCULATOR")
weight = int(input("How much do yo weigh in kilograms?"))
height = float(input("How tall are you in meters?"))
#weight = 78
#height = 46
bmi = weight / (height*height)

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are in the normal weight range.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")

#Sum of Consecutive Numbers 
#Take a number N as input and output the sum of all numbers from 1 to N (including N).
print("SUM OF CONSECUTIVE NUMBERS")
N = int(input("Input a number and I will tell you the sum of all numbers from 1 to that number..."))
#N = 4
sum = 0
numbers = range(1, N+1)
for num in numbers:
    sum = sum + num 
    if num == N:
        print("The sum of all numbers from 1 to " + str(N) + " is equal to " + str(sum))


#Search Engine
#Takes a text and a word as input and passes them to a function called search().
#The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
print("SEARCH ENGINE")    

#text = input("Input text to search within...")
text = "Let's play a LoveGame. Do you want love, or you want fame?"
#word = input("Input word you are searching for...")
word = "Love"
def search(text,word): 
    if word in text:
        return("Word found")
    elif word not in text:
        return("Word not found")
    else:
        pass

print(search(text, word))

