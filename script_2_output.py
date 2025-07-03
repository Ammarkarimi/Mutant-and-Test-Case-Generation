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


def test():
    # Equilateral triangle
    assert triangle(2, 2, 2) == 0
    assert triangle(10, 10, 10) == 0
    assert triangle(100, 100, 100) == 0
    
    # Isosceles triangle
    assert triangle(2, 2, 3) == 1
    assert triangle(5, 5, 7) == 1
    assert triangle(8, 6, 8) == 1
    
    # Scalene triangle
    assert triangle(2, 3, 4) == 2
    assert triangle(7, 10, 5) == 2
    assert triangle(12, 15, 18) == 2
    
    # Invalid triangle
    assert triangle(1, 2, 4) == 3
    assert triangle(5, 10, 25) == 3
    assert triangle(8, 8, 16) == 3
    
    # Additional test cases
    assert triangle(0, 0, 0) == 3  # All sides zero
    assert triangle(1, 2, 3) == 3  # Sum of two sides equals the third side
    assert triangle(10, 20, 30) == 3  # Sum of two sides less than the third side
    assert triangle(-1, 2, 3) == 3  # Negative side length
    assert triangle(5, -5, 5) == 3  # Negative side length