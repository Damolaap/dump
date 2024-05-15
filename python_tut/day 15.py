# polymorphism : method overiding method over loading

'''
class Parent:
    color =  'Yellow'
    skin = 'Dark'

    def can_eat(self):
        return True
    def can_run(self):

        def __init__(self):
            self.first_name = 'damola'

class FirstChild(Parent):
    color = '#fff'
    def is_a_writer(self):
        return False

    def get_color(self):
        return self.color

    def get_color(self):
        return super().color # you can specify the parent in it

    def can_run(self):
        super().can_run()

        f = FirstChild()
        print(f.get_color())

class Parent:
    color =  'Yellow'
    skin = 'Dark'

    def can_eat(self):
        return True
    def can_run(self):

        def __init__(self):
            self.first_name = 'damola'

class FirstChild(Parent):
    color = '#fff'
    def is_a_writer(self):
        return False
'''

'''
from time import sleep
sleep(3)
print('Damola is a good boy')

sleep(3)
print('eh choke')
'''

'''
from time import sleep
num = int(input('Enter any number: '))

for i in range(1, num):
    sleep(0.5)
    print(i ** 2)
'''

'''
#program that checks how long it takes me to type something using the time module
from time import time
print('TYPE: "This is a test!"')
start_time = time()
user_input = input('Type: ')
stop_time = time()
print(f'It took you {round(stop_time - start_time)} seconds')#round() this rounds up float numbers
'''

'''
#to get the number of words per minute
from time import time
print('TYPE: "This is a test!"')
start_time = time()
user_input = input('Type: ')
stop_time = time()
time_taken = round(stop_time - start_time)
char_len = len(user_input)
words_per_min = (char_len/time_taken)/60
print(f'You are typing at {words_per_min} words per minute.')
'''

from time import sleep
while True:
    sleep(1)
    print('Loading.  ', end='\r')
    sleep(1)
    print('Loading.. ', end='\r')
    sleep(1)
    print('Loading...', end='\r')

































