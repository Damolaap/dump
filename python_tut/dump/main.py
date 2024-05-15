'''
def custom_range():
    for i in range(1, 101):
        yield [i ** 2, i ** 3, i ** 4]

#print("Name: ", __name__)
print("File: ", __file__)
        
def dump_func():
    print('Hello Everyone')
'''

import module_tut
result_add = module_tut.add(4,5)
result_subtract = module_tut.subtract(12,6)
print(f'Addition:{result_add}\nSubtraction:{result_subtract}')
