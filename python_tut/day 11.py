#create a program that calculates the factorial of a number
'''
num = int(input('enter a number: '))
factorial = num
for i in range(num -1, 1, -1):
    factorial *= i   
print(factorial)
'''

'''
#with while loop
num = int(input('enter a number: '))
factorial = num
count = num
while count > 1:
    count -= 1
    factorial *= count
print(factorial)
'''

'''
#math module
num = int(input("enter any number to find it's factorial: "))
import math
#dir(math) gives the funtions available in this module
print(math.factorial(num))
'''

'''
import math
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
print(dir(math))
'''


'''
import string
pass_len = 12
import random
print('for only uppercase enter 1,\n
for upper and lower case enter 2,\n
for upper case,lower case and digits enter 3,\n
for upper case,lower case, digits and punctuations enter 4: ')
user_choice = input('enter your choice: ')

if user_choice == '1':
    upper_case = random.sample(string.ascii_uppercase, 12)
    passwrd = upper_case
    print(''.join(passwrd))
    
elif user_choice == '2':
    upper_case = random.sample(string.ascii_uppercase, 6)
    lower_case = random.sample(string.ascii_lowercase, 6)
    passwrd = upper_case + lower_case
    print(''.join(passwrd))

elif user_choice == '3':
    upper_case = random.sample(string.ascii_uppercase, 2)
    lower_case = random.sample(string.ascii_lowercase, 8)
    digits = random.sample(string.digits, 2)
    passwrd = upper_case + lower_case + digits
    print(''.join(passwrd))

elif user_choice == '4':        
    upper_case = random.sample(string.ascii_uppercase, 1)
    lower_case = random.sample(string.ascii_lowercase, 7)
    digits = random.sample(string.digits, 2)
    punctuations = random.sample(string.punctuation, 2)
    passwrd = upper_case + lower_case + digits + punctuations
    print(''.join(passwrd))
'''

'''
#building a password list (4 digits)
#exception or error handling
try:
    txt_file = open('C:\\Users\\Alhaji Apex\\Desktop\\Python tut\\dump.txt', 'w') #tells the code to open in write mode
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for m in range(10):
                    for n in range(10):
                        txt_file.write(f'{i}{j}{k}{m}{n}\n')
                    
    txt_file.close()

except:
    print('an error occured')
#else
#finally
'''

'''
a_z = []
from string import ascii_lowercase, ascii_uppercase
alph_upper = ascii_uppercase
alph_lower = ascii_lowercase
for i in range(26):
    alphabet = alph_upper[i] + alph_lower[i]
    a_z.append(alphabet)
print(' '.join(a_z))
'''














        
