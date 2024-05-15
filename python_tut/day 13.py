#modules : a way to organize code!
#generators use yield and are in loops, they dont need to be called
'''
def custom_range(start, stop, step):

    for i in range(start, stop, step):
        yield i ** 2

for each_value in custom_range(10, 100, 2):
    print(each_value)
'''

#a class is a blueprint for creating objects
#creating classes
#by cinvention first letter of your class name should be in upper case and you dont need to use under score
#variables defined in a class are called fields
#functions in a class are called methods

'''
class MyClass :
    f1 = 'Test'
    f2 = 'Random'

cn1 = MyClass()
cn1.f1 = 'Heyyy'
print('F1 in cn1 is >>> ', cn1.f1)
'''


class CarFactory :
    eng = 'V12'
    whldrv = 'Four wheel drive'
    tyre = 'Medium hard tyres'
    vehtyp = 'Sport car'
    def hrspw(self):
        print(self.eng)
    #use '(self)' in a class : this method should be accessible when an object calls : else call the classname '.' the function name
    #varialble defined in a function is called a local variable else a global data
   
        
corvette = CarFactory()
corvette.eng = 'V8'
#corvette.hrspw()
#print(corvette.eng)

CarFactory.hrspw()
#Inheritance, Encapsulation, Abstraction, Polymorphism : classes is needed to implement them


















