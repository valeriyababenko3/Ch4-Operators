'''
100 equals 100.0 ? True
100 is the same object as 100.0 ? False


'''
x = 100
y = 200
z = 2.71828
t = 3.14159
num1 = 100
num2 = 100.0

print( f'{x} times {z}= {x*z}')
print( f'{x} divided by {z}= {x/z}')
print( f'{z} raised to the power of {t} to 6 decimals = {z ** t:.6f}')
print( f'{x} plus {y} multiplied by {z} = {(x+y)*z}')
print( f'{x} plus {y} divided by {z} plus {t} = {(x+y)/(z+t)}')
print( f'{x} divided by {z} plus {y} divided by {t} = {(x/z + y/t)}')
print (f' Is {x} less than {y} ? {x<y}')
print (f' Is {x} greater than {z}  OR {t} equal to {y}? { x>z or t==y}')
print (f' Is {x} cubed greater than {y} squared? {x**4 > y**2}')
print (f' Is True grester than false? { True> False}')
string1 = "abcdef"
print (f' The letter "f" in {string1}? "f" is {string1}')
print (f' The letter "k" is NOT in {string1}? "k" is Not in  {string1}')
print (f' {num1} equals to {num2}? { num1 == num2}')
print (f' Is {num1} is tje same object as {num2}? {num1 != num2}')

'''
Part 2
Write a Python program that converts Celsius to Fahrenheit by using the 
following formula:
Faren = ( ( 9 * Cels) / 5 ) + 32
Prompt the user for a Celsius temperature. Remember that user input is returned 
as a character string and must be converted!
The program may be done in two lines
'''

cels= float(input("Enter Celsius Temperature :"))
fahr= ((9 * cels / 5) +32)
celssymb = "\u00b0C"
fahrsymb = "\u00b0F"
print (f'{cels} {celssymb} = {fahr} {fahrsymb}')

