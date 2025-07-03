# Constants to represent triangle types
EQUILATERAL = 0
ISOSCELES = 1
SCALENE = 2
INVALID = 3

def triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return INVALID
    if a == b and b == c:
        return EQUILATERAL
    if a == b or a == c or b == c:
        return ISOSCELES
    return SCALENE
