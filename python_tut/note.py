# print('This is a love calculator :)')
# start_calc = input('Do you want to try the Love Calculator: yes/no ').lower()

# if start_calc == 'yes':
#     print('The love calculator is calculating your score...')
#     name1 = input('What is your name? ').lower()
#     name2 = input('what is your name? ').lower()
#     #true love...

#     t_cnt = (name1).count('t')
#     r_cnt = (name1).count('r')
#     u_cnt = (name1).count('u')
#     e_cnt = (name1).count('e')

#     l_cnt = (name2).count('l')
#     o_cnt = (name2).count('o')
#     v_cnt = (name2).count('v')
#     e_cnt = (name2).count('e')

#     true_cnt = int(t_cnt + r_cnt + u_cnt + e_cnt)
#     love_cnt = int(l_cnt + o_cnt + v_cnt + e_cnt)
#     cnt = int(str(true_cnt) + str(love_cnt))
#     if cnt < 10 or cnt > 90:
#         print(f'Your score is {cnt}, You are like coke and mentos :)')
#     elif cnt >= 40 or cnt <= 50:
#         print(f'Your score is {cnt}, You are a good match :)')
#     else:
#         print(f'Your score is {cnt}')
# elif start_calc == 'no':
#     print('Goodbye')
# else:
#     print('invalid input')

'''
print('Welcome to treasure island.\nYour mission is to find the Treasure :)')

user_input = input('Enter "left" or "right" to proceed: ')
if user_input == 'left':
    user_input = input('Enter "swim" or "wait" to proceed: ')
    if user_input == 'wait':
        user_input = input('Pick a door red, blue, yellow')
        if user_input == 'yellow':
            print('You win!')
        elif user_input == 'red' or user_input == 'blue':
            print('Game Over!')
        else:
            print('Invalid input!')
    elif user_input == 'swim':
        print('Game Over')
    else:
        print('Invalid input')
        
elif user_input == 'right':
    print('Game Over!')
    
else:
    print('invalid input')
'''


'''
#Algorithm is a set of steps to solve a problem
    Step 1. Start
    Step 2. Input radius, R
    Step 3. A <- 3.14 x R x R
    Step 4. Print Area, A
    Step 5. Stoph
'''

'''
import random

def num_guessing_game():
    print('Welcome to the number guessing game')
    target_number = random.randint(1,100)
    attempts = 0
    
    try:
        while True:
            user_guess = int(input('Guess the number (1-100): '))
            attempts += 1
            if user_guess == target_number:
                print(f'congratulations you just guessed the correct number! {target_number} in {attempts} attempts.')
                break
            elif user_guess < target_number:
                print('Too Low, Try again.')
            else:
                print('Too high, Try again')
    except ValueEroor:
        print('Error: enter a valid number')
        
num_guessing_game()
'''

#in files r for read w for write a for append
'''
with open('dump.txt', 'r') as file:
    content = file.read()
    print(content)
'''
'''
with open('dump.txt', 'w') as file:
    file.write('Hello, This is a sample text.')
'''
'''
with open('dump.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        print(line.strip())#prints out the content in a file in a sorted way i guess
'''
'''
file_path = 'dump.txt'
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content.)
except FileNotFoundError:
    print(f'File not found: {file_path}')
'''

'''
import csv
data = [
    ['Name', 'Age', 'City']'
    ['Alice', 25, 'New York']
    ['Bob', 45, 'San Francisco']
    ['Charlie', 50, 'Los Angeles']
]

with open()
'''
'''
import random
from datetime import datetime
import os

current_time = datetime.now()
print(f'Current time: {current_time}')

current_dir = os.getcwd()
print(f'Current directory: {current_dir}')
'''

'''
#note taking app \cli proj
import os

def display_menu():
    print('\nNote-Taking App')
    print('1. View Notes')
    print('2. Add note')
    print('3. Delete Note')
    print('4. Exit')

def view_note():
    print('\nExisting notes are the following')
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        print('No notes available')
        return
    for filename in os.listdir(notes_dir):
        with open(os.path.join(notes_dir,filename), 'r') as file:
            content = file.read
            print(f'{filename[-4]}: {content}')

def add_note():
    note_title = input('Enter the note Title: ')
    note_content = input('Enter the note content: ')

    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    note_path = os.path.join(notes_dir, f'{note_title}.txt')
    with open(note_path, 'a') as file:
        file.write(f'{note_content}\n')

    print(f'Note {note_title} added successfully')

def delete_note():
    note_title = input('Enter the title of the note to delete: ')
    notes_dir = 'notes'
    notes_path = os.path.join(notes_dir, f'{note_title}.txt')

    if os.path.exists(notes_path):
        os.remove(notes_path)
        print(f'Note {note_title} deleted successfully.')
    else:
        print(f'Note {note_title} not found.')

def main():

    while True:
        display_menu()
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            view_note()
        elif choice == '2':
            add_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print('Exiting the Note-taking App. goodBye')
            break
        else:
            print('Invalid choice. please enter number between 1 and 4')


if __name__ == '__main__':
    main()
'''

'''
#a class is a blueprint for creating objects

class Car: #super class
    def __init__(self, make, model, year):
        #constractor
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'{self.year} {self.make} {self.model}')
        # an object is an instance of a class with its own set of attributes and methods

car1 = Car('Toyota', 'Camry', 2022)
car2 = Car('Ford', 'Mustang', 2021)

#car1.display_info()
#car2.display_info()

#inheritnace

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f'Battery capacity: {self.battery_capacity} kwh')


Electric_car = ElectricCar('Toyota', 'Camry', 2022, 5000)
Electric_car.display_info()
'''

'''
class Transaction:
    def __init__(self,  amount,  transaction_type):
        self.amount =  amount
        self.transaction_type = transaction_type
        

class Account:
    def __init__(self, account_number,  holder_name, balance =  0):
        self.account_number = account_number
        self.holder_number = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, 'Deposit'))
            print(f'Deposit of ${amount} Successful. New balance: ${self.balance}')
        else:
            print('invalid deposit amount')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'Withdrawal'))
            print(f'Withdrawal of ${amount} successful. New balance: ${self.balance}')
        else:
            print('invalid withdrawal amount or insufficient funds')
    def display_transactions(self):
        print('\nTransaction History: ')
        for transaction in self.transactions:
            print(f'${transaction.amount} {transaction.transaction_type}')
    def display_balance(self):
        print(f'\nCurrent balance for Account {self.account_number}: ${self.balance}')

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance = 0):
        if account_number not in self.accounts:
            new_account = Account(account_number, holder_name, initial_balance)
            self.accounts[account_number] = new_account
            print(f'Account created successfully for {holder_name}. Account number: {account_number}')
        else:
            print(f'Account with the given number exists.')

    def get_account(self, account_number):
        return self.accounts.get(account_number)

bank = Bank('GT Bank')

#create account
dam_account = bank.create_account(1234567890, 'Adedamola', 50000)
ola_account = bank.create_account(9162351078, 'Damola')

#accessing account
dam_account = bank.get_account(1234567890)
ola_account = bank.get_account(9162351078)

#making transactions
dam_account.deposit(500)
dam_account.withdraw(200)

ola_account.deposit(1000)
ola_account.withdraw(300)

# display transaction history and balances
dam_account.display_transactions()
dam_account.display_balance()

ola_account.display_transactions()
ola_account.display_balance()
'''

#APIs - Application Programming Interface - a way for two or more computer to communicate with each other
#remote api
#open api (ai shi...)
#public api
#private api

#https://api.coinbase.com/v2/prices/buy?currency=USD
#8526878b-0f23-4c45-8fbc-821d48c2d371
'''
import requests
import apikey
import turtle


url = 'https://api.coinbase.com/v2/prices/buy?currency=USD'

json = requests.get(url)
print(json)
'''

#response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
#print(response)

#error with this shii
'''
import vonage

client = vonage.Client(key='216f18a5', secret='pfa4bmjlAjT5M3CK')

sms = vonage.Sms(client)

responseData = sms.send_message(
    {
      'from' : 'VONAGE APIS',
      'to' : '+2349162351078',
      'text' : 'a text from vonage as a test!'
    }
)

if responseData['messages'][0]['status'] == 0:    
    print('message sent successfully')
#else:
    #print(f'message failed with error: {responseData['messages'][0]['error-text']}')
'''

'''
def complex_calculation(a, b):
    intermediate_result = a * 2
    print(f'Intermediate Result: {intermediate_result}')

    final_result = intermediate_result + b
    print(f'Final Result: {final_result}')

    return final_result

result = complex_calculation(5, 10)
print(f'Final output: {result}')
'''

'''
user_input = str(input('Enter a phrase: '))
text = user_input.split()
a = ''
for i in text:
    a = a+str(i[0]).upper()
print(a)
'''





















    












