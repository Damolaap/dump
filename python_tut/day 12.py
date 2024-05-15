'''
def arg_sum(num1, num2):
    sum_num = num1 + num2
    print(sum_num)

arg_sum(1,2)
'''

#arguments
'''
def myfunc(*args):
    value = 0
    for items in args:
        value += items
    print(value)
        
myfunc(1,2,3,4,5)

def myfunc(a, **kwargs):
    print('A: ', a)
    print(kwargs)
'''

#lambda
'''
a = lambda x, y: print(x + y)
a(1, 2)
'''

def mylist():
    listss = [[0,1,2,3,4],[5,6,7,8,9]]
    print('[', listss[0], listss[1],']',sep='\n')
    
mylist()
