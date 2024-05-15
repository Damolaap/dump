
#name = input("Enter username: ")

#program to print first and last name
'''
first_name = input("enter firstname: ")
last_name = input("enter lastname: ")
print("First name = " + first_name)
print("Last name = " + last_name)
'''

#program to convert kg to pounds and gram
'''
weight_in_kg = float(input("Enter weight in Kg "))
weight_in_pounds = str(weight_in_kg * 2.2)
weight_in_gram = str(weight_in_kg * 100)
print(weight_in_pounds + "Pounds")
print(weight_in_gram + "g")
'''

#program to convert naira to dollar
'''
value_in_NGN = float(input("Enter value in NGN: "))
value_in_USD = str(value_in_NGN * 1100)
print("$" + value_in_USD)
'''

#program to replicate strings
'''
number_of_replicates = int(input("Number of replicates: "))
string_to_be_replicated = input("Enter string to be replicated: ") * number_of_replicates
print(string_to_be_replicated)
'''

#program to calculate quadratic equations
'''
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
quadratic_equation_neg = (-b - (b ** 2 - (4 * a * c)) ** 0.5) / 2 * a
quadratic_equation_pos = (-b + (b ** 2 - (4 * a * c)) ** 0.5) / 2 * a
print("x = " + str(quadratic_equation_neg))
print("y = " + str(quadratic_equation_pos))
'''

#program to convert centigrade to kelvin
'''
value_in_C = float(input("Enter value in centigrade: "))
value_in_K = value_in_C + 273.15
print(str(value_in_K) + "Kelvin")
'''
#program that prints the square of a number in full sentence
'''
number = float(input("Enter a number: "))
square_of_number = number ** 2
print("The square of the number is ",square_of_number,".",sep="")
'''

#program to print a number x, seperated by three dashes
'''
number = int(input("Enter a number x: "))
print(number, 2 * number, 3 * number, 4 * number, 5 * number, sep="---")
'''
