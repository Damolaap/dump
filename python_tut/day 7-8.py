#program to input day of the week using a match statement
'''
date = input('enter any number from 1-7: ')
match date:
    case '1':
        print('monday')
    case '2':
        print('tuesday')
    case '3':
        print('wednesday')
    case '4':
        print('thursday')
    case '5':
        print('friday')
    case '6':
        print('saturday')
    case '7':
        print('sunday')
    case other:
        print('invalid')
'''

#grade of students
'''
grade = int(input('enter grade 1-5: '))
match grade:
    case 1:
        print('very good')
    case 2:
        print('good')
    case 3:
        print('not bad')
    case 4:
        print('bad')
    case 5:
        print('very bad')
    case other:
        print('invalid input!')
'''

#a for loop that doees not seperate lines but uses a space
'''
for i in range(0,11):
    print(i,end=' ')
'''


# this prints my name 100 times
'''
for i in range(0,101):
    print('damola')
'''

'''
name = input('Enter a word: ')
for i in range(1,51):
    print(i,', ',name,sep='')
'''

'''
even_num = int(input('enter any number: ')) + 1
for i in range(0,even_num):
    if i % 2 == 0:
        print(i)
'''

# this prints out asterixs instead of a
'''
for i in range(0,7):
    print('*' * i)
'''

'''
multiples = int(input('enter any number: '))
for i in range(1,13):
    print (i, 'X', multiples,'=',(i * multiples))
'''

from random import randint
user_score = 0
for i in range(11):
    comp_guess = randint(0,10)
    print(comp_guess)
    user_guess = int(input('enter any number from 1- 10: '))
    if user_guess == comp_guess:
        user_score += 5
        print('correct')
    else:
        user_score -= 2
        print('wrong')
print('user score is ', user_score)
