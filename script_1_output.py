def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False



def test():
    # Test cases for any_int function
    assert any_int(2, 3, 5) == True  # 2 + 3 = 5
    assert any_int(-2, 3, 1) == True  # -2 + 3 = 1
    assert any_int(0, 0, 0) == True  # 0 + 0 = 0
    assert any_int(-2, 5, -3) == False  # -2 + 5 != -3
    assert any_int(2, 2, 3) == False  # Not possible to form a valid equation
    assert any_int(1, 1, 2) == True  # 1 + 1 = 2
    assert any_int(3, 4, 7) == True  # 3 + 4 = 7
    assert any_int(-5, -3, -8) == True  # -5 + (-3) = -8
    assert any_int(10, 10, 20) == True  # 10 + 10 = 20
    assert any_int(100, 200, 301) == False  # 100, 200 and 301 doesn't form a valid equation
    assert any_int(1, 2, 4) == False  # 1, 2 and 4 doesn't form a valid equation
    assert any_int(0, -1, -1) == True  # 0 + (-1) = -1
    assert any_int(2147483647, -2147483647, 0) == True  # Maximum and minimum integer values used
    assert any_int(2147483647, 2147483647, 4294967294) == True  # Maximum integer values forming a valid equation
    assert any_int(-2147483648, 0, -2147483648) == True  # Minimum and maximum integer values used
    assert any_int(1, -1, 0) == True  # 1 + (-1) = 0
    assert any_int(-1, 1, 0) == True  # -1 + 1 = 0
    assert any_int(0, 1, 1) == True  # 0 + 1 = 1 (Zero handling)
    assert any_int(1, 0, 1) == True  # 1 + 0 = 1 (Zero handling)
    assert any_int(0, 1, 2) == False  # 0 + 1 != 2 (Negative handling)
    assert any_int(1, -1, -2) == False  # 1 + (-1) != -2 (Negative handling)
    assert any_int(-2147483648, -2147483648, -4294967295) == False  # Negative values forming an invalid equation
    assert any_int(2147483647, 2147483647, -4294967295) == False  # Maximum values forming an invalid equation
    assert any_int(2147483647, -2147483647, 0) == False  # Maximum and minimum values forming an invalid equation
    assert any_int(2147483647, 2147483647, 4294967295) == False  # Maximum values forming an invalid equation
    
    test()