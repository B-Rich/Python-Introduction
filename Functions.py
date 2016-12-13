# Python 3.5.2
# Functions Examples

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
