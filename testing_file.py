def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False



def test():
    # Correctness and negative handling
    assert any_int(-1, 0, 1) == False  # Testing negative, zero, positive numbers with no sum
    assert any_int(0, 0, 1) == False  # Testing zeros with positive number and no sum
    assert any_int(0, -1, 0) == False  # Testing zero with negative numbers and no sum
    
    # Edge Cases
    assert any_int(-2147483648, -2147483648, 2147483647) == True  # Testing two minimum possible values with maximum possible value and sum
    assert any_int(2147483647, 2147483647, -2147483648) == True  # Testing two maximum possible values with minimum possible value and sum
    
    # Variety
    assert any_int(2, 3, 5) == False  # Testing for another set of invalid sum
    assert any_int(0, -2147483648, 0) == False  # Testing zero with minimum possible value and no sum
    assert any_int(2147483647, 0, 0) == False  # Testing maximum possible value with zeros and no sum
    assert any_int(0, 2, -2) == True  # Testing zero with positive and negative numbers and zero sum
    assert any_int(3, 4, 7) == True  # Testing another set of positive numbers with sum
    assert any_int(-3, -4, -7) == True  # Testing another set of negative numbers with sum
    
    # Additional test cases for full coverage
    assert any_int(0, 0, 0) == True  # Testing zeros with zero sum
    assert any_int(-2147483648, -2147483648, -2147483648) == True  # Testing three minimum possible values with sum
    assert any_int(2147483647, 0, -2147483648) == True  # Testing maximum possible value with zero and minimum possible value with sum
    assert any_int(0, 0, -1) == False  # Testing zeros with negative number and no sum
    assert any_int(-2147483648, -2147483648, -2147483647) == False  # Testing two minimum possible values with one less than minimum value and no sum