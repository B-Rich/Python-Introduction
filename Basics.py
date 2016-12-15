# Version: Python 3.5.2
# TITLE: Basics

####################
# SECTION: Hello World!

print("Hello World!")

####################
# SECTION: Arithmetic Operations

#   +   plus            addition
#   -   minus           subtraction
#   *   times           multiplication
#   /   divided by      subtraction
#   **   power          exponentiation

# Operator Precedence = (), **, *, /, +, -

print (3+4) # Prints 7
print (type(3+4)) # int

print (3-2) # Prints 1
print (type(3-2)) # int

print (3*4) # Prints 12
print (type(3*4)) # Prints 12

print (9/3) # Prints 3.0
print (type(9/3)) # float

print (9/4) # Prints 2.25
print (type(9/4)) # float

print (9.0/3.0) # Prints 3.0
print (type(9.0/3.0)) # float

print (3**4) # Prints 81
print (type(3**4)) # int

# Variable Incrementation

x = 1
print (x) # 1
x = x + 1
print (x) # 2
x += 1;
print (x) # 3

####################
# SECTION: Functions

# Compute the area of a rectangle.
def rectangle_area(base, height):     
    area = base * height 
    return area

# Convert Fahrenheit to Celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# Convert Celsius to Fahrenheit
def celsius2fahrenheit(celsius):
    fahrenheit = (9.0 / 5) * (celsius + 32)
    return fahrenheit

# Convert Fahrenheit to Kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# TEST.
print (rectangle_area(3, 8))

print (fahrenheit2celsius(32))
print (celsius2fahrenheit(37))
print (fahrenheit2kelvin(32))

# This is also possible.
print (fahrenheit2kelvin(celsius2fahrenheit(0)))

# A Function without a return value returns None.
def noneReturn():
    print ("Next line is going to be 'None'")

test = noneReturn()
print (test);

