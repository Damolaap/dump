# build a image resizer
# pillow module
import time
from PIL import Image

img = Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Koala.jpg')

'''
#resize and thumbmail method uses a tuple as input
print('Resizing...')
time.sleep(2)
w, h = img.size#it returns the size of the image
myimg = img.crop((500, 50, 100+w, 50+h))
#img.thumbnail((400, 400))

myimg.save('C:\\Users\\Public\\Pictures\\Sample Pictures\\Koala_mod.jpg')
print('Saved')
'''

'''
#img.show('Image.jpg')
from requests import get
from pprint import pprint
from quiz import quiz

try:
    #quiz_url = ('https://the-trivia-api.com/v2/questions/')
    #result = get(quiz_url).json()
    result = quiz
    score = 0
    
    for items in result:
        user_choice = items['incorrectAnswers']
        user_choice.append(items['correctAnswer'])
        pprint(items['question']['text'])
        print(user_choice,'\n')
        user_input = input('Enter the correct answer: ')

        if user_input.upper() == items['correctAnswer'].upper():
            score += 10
            print('Correct\n')
        elif user_input.upper() != items['correctAnswer'].upper():
            print(f'wrong, Correct answer is {items["correctAnswer"]}\n')
        else:
            print('invalid choice\n')
    score_percent = (score/100)*100
    print(f'Score: {score_percent}%')
    
except ConnectionError:
    print('No internet Connection')
'''

from requests import get
url = 'https://chain.api.btc.com/v3/block/latest'
print(get(url))










































