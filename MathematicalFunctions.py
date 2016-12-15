# Python 3.5.2
# Mathematical Function Examples

# Compute the smaller root of a quadratic equation.
def smaller_root(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if (discriminant < 0 or a == 0):
        print ("ERROR: No Real Solution exists.")
    else:
        discriminant_sqrt = discriminant ** 0.5
        if a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)

# Compute the area of a rectangle.
def rectangle_area(base, height):     
    area = base * height 
    return area

# Compute the area of polygon with equal sides
def area(number_of_sides, side_length):
    return (number_of_sides * side_length ** 2) / (4 * math.tan(math.pi/n))

# Test
print (smaller_root(1, 2, 3))
print (smaller_root(4, 24, 2))
print (area(7, 3))
