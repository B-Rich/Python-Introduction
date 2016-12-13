# Python 3.5.2
# Functions Examples

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

# Test
def test(a, b, c):
    print ("The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c)) 
    print (str(smaller_root(a, b, c)))       

test(1, 2, 3)
test(5, 3, -20)
test(4, 24, 2)
