# a prgram that distinguishes students based on their number of credits
'''
credits_taken = int(input("input number of credits taken: "))
if credits_taken < 1:
    print("invalid input")
elif credits_taken <= 23:
    print("student is a freshman")
elif credits_taken >= 24 and credits_taken <= 53:
    print("student is a second-year student")
elif credits_taken >= 54 and credits_taken <= 83:
    print("student is a junior")
elif credits_taken >= 84:
    print("student is a senior")
'''

# a program that tells is a year is a leap year
'''
year = int(input("enter the year: "))
if year % 4 == 0:
    print("it is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")
#another way
if (year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)
'''

# a temperature scale
'''
temp_in_c = float(input("input temperature in Celsius: "))
if temp_in_c < -273.15:
    print("temperaure is invalid because it is below absolute zero")
elif temp_in_c == -273.15:
    print("temperature is absolute zero")
elif temp_in_c >= -273.15 and temp_in_c < 0:
    print("temperature is below freezing")
elif temp_in_c == 0:
    print("temperature is at freezing point")
elif temp_in_c > 0 and temp_in_c <= 100:
    print("temperature is in normal range")
elif temp_in_c == 100:
    print("temperature is at boiling point")
elif temp_in_c > 100:
    print("temperature is above boiling point")
'''

# a number guessing game
'''
from random import randint
random_number = randint(0,10)
guessed_number = int(input("enter any number: "))
if guessed_number == random_number:
    print("correct")
else:
    print("wrong")
'''

# difference is it displays the random number beore you input your gusee
'''
from random import randint
random_number = randint(0,10)
print (random_number)
guessed_number = int(input("enter any number: "))
if guessed_number == random_number:
    print("correct")
else:
    print("wrong")
'''

# generates two random numbers and displays them and their sum
'''
from random import randint
a = randint(0,10)
b = randint(0,10)
print (a,b)
print (a + b)
'''

#rock paper scissors game
'''
from random import randint
rock = 1
papper = 2
paper = 3
comp_choice = randint(1,3)
my_choice = int(input("enter any number from 1-3: "))
print (comp_choice,my_choice)
if comp_choice == my_choice:
    print("won")
else:
    print("lost")
'''

#dice roll game
'''
from random import randint
c1 = randint(1,6)
c2 = randint(1,6)
u1 = randint(1,6)
u2 = randint(1,6)
c = c1 + c2
u = u1 + u2
print(c,u)
if c > u:
    print("lost")
elif u > c:
    print("won")
elif c == u:
    print("tie")
'''

#string manipulation, slicing, indexing
#it searches for a character in a string
'''
string = "this is valuemax coders hub".upper()
search = input("input a letter: ").upper()
print(string.find(search))
'''
