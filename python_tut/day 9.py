'''
a = 'damola'
for character in a:
    print(character)

for i in range(0,len(a)):
    print(a[i])
'''

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(my_list[0 : len(my_list) : 2])

for i in range(len(my_list)):
    print(my_list[i])
    
for i in range(10):
    print(my_list[i])
'''

'''
my_list = []
for i in range(3, 301, 3):
    my_list.append(i)
print(my_list)
'''

'''
from random import randint
rand_num0 = []
rand_num1 = []

#this produces 10 random numbers and it appends them as different items into a list then sorts them.
for i in range(10):
    a = randint(0,9)
    rand_num0.append(a)
    rand_num0.sort()

#this creates a loop that inserts each item to the first place in a list there printing it in descending order
for item in rand_num0:
    rand_num1.insert(0, item)
print(rand_num1)
'''

