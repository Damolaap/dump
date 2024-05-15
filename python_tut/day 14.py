#an array is a collection of items stored in a ....
#python package manager (pip) is used to install modules
#setattr()...getattr(): check em out,
'''
d1 = DemoClass('tobbs', 'testing it')

for i in range(15):
    setaatr(d1, f'num{i}', i**3)

print(getattr(d1, 'num3')
#__init__(): doesnt return anything, __str__ methods
#in classes
'''

'''
def __init__(): #this method is only used in a class cause that is what it is designed for! used if we want something to happen immediately we ctreate an object
    print('Hello World')
'''

#CLI - command line interface
#GUI - graphical user interface
#CUI - character user interface
#web app
#mobile
#API - application programming interface

#web scraping : taking data from websites by making a request to that site
#website is down checker
#use of request module
#pip install module name

'''
import requests

try:
    web_url = input('Enter web url: ')
    web_req = requests.get(web_url)
    web_sta = web_req.status_code
    
    if web_sta == 200:
        print('Website is running!')
    else:
        print('website is down!')
    #print(web_req)
except:
    print('cannot connect to internet!')
'''
#print in a nice way ig

import requests
from pprint import pprint
base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
user_src = input('Enter a word: ')
base_url += user_src
#base_url = base_url + user_src
#json: lists and dictionaries


try:
    print('Definitions: ')
    count = 0
    result = requests.get(base_url).json()
    
    for items in result:
        for meaning in items['meanings']:
            for definitions in meaning['definitions']:
                count += 1
                print(f"{count}. {definitions['definition']}")
                
    print('Examples:')
    count = 0
    for items in result:
        for meaning in items['meanings']:
            for examples in meaning['definitions']:
                if 'example' in examples:
                    count += 1
                    print(f"{count}.", examples['example'])

                        
                #for i in things:
                    #print(i)
                #count += 1
             
        #pprint(items['meanings'][1]['definitions'][0]['definition'])
except ConnectionError:
    print('error occured')































