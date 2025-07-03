python
def triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return INVALID
    if a == b and b == c:
        return EQUILATERAL
    if a == b or a == c or b == c:
        return EQUILATERAL
    return SCALENE
