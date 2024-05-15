#dimentional lists: linear/ 1 dimensional lists

'''
a = []
for i in range(1,31):
    b = (i, i * i)
    a.append(b)
print(a)
'''

'''
a = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 0]
print(tuple(a))
'''

'''
a = 4
b = 8

hold = a
a = b
b = hold

#tuple unpacking/// works with a list too!
(a, b) = (b, a)
print(a, b)
'''

'''
#sets
from random import randint
'''

'''
#dictionary: to order data...key(word) >>> value(meaning)
a = {'name' : 'damola', 1 : 20009, 5 : 800*6, 'name' : 'kjdhsudgs'}
b = a.pop('name')#stores on the value of the key
a.update({'name : b'})
a.values#print out the values into a list
a.keys#prints outs the keys into a list
a.popitem()#removes the last key value pair
print(a.get('name', 'N/A'))#checks is a key exists in a dictionary and returns its value. other wise, it returns the value in the other argument
'''

'''
a = {'name' : 'damola', 1 : 20009, 5 : 800*6, 'name' : 'kjdhsudgs'}
for key, value, in a.items():
    print(key, '>>>', value)
'''

'''
a = {}
for i in range(1,31):
    key = i
    value = i - 1
    a.update({key : value})
print(a)
'''

'''
#list comprehension
[var loop if]...when using if...else = [var i...else loop]
b = [j ** 2 for j in range(50) if ((j ** 2) % 10) % 2 == 0 ]
print(b)
'''
#to get last number is integer % 10, 2...int % 100 and so on

#write a program that takes in a number and brings back a list of prime numbers within that range
'''
prime = []
for num in range(1,51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)
print(prime)
'''

'''
users = [{'name':'damola', 'gender':'male', 'email':'damolaap', 'password':'12345'}]
#sign up or login system
user_choice = input("enter 'y' for sign up or 'n' for login option: ")

if user_choice == 'y':
    name = input('enter user name: ')
    gender = input('enter user gender: ')
    email = input('enter user email: ')
    password = input('enter user password: ')
    new_credentials = {'name':name, 'gender':gender, 'email':email, 'password':password}
    users.append(new_credentials)
    print('signed up successfully! :)')
    
        
    print('login into the system after sign up')
    new_login_email = input('enter new user email: ')
    new_login_pass = input('enter new user password: ')
    for user in users:
        if user['email'] == new_login_email and user['password'] == new_login_pass:
            print('login successful! :)')
            break
        else:
            pass
    else:
        print('invalid credentials! :(')
            
elif user_choice == 'n':
    login_email = input('enter user email: ')
    login_pass = input('enter user password: ')
    for user in users:
        if user['email'] == login_email and user['password'] == login_pass:
            print('login successful! :)')
            break
        else:
            pass
    else:
        print('invalid credentials! :(')
            
else:
    print('invalid input!')
'''
