def add_or_subtract(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    else:
        return "Invalid operation. Use '+' or '-'"


def test():
    # Test for addition operation
    assert add_or_subtract(5, 3, '+') == 8
    assert add_or_subtract(-2, 7, '+') == 5
    assert add_or_subtract(0, 0, '+') == 0
    
    # Test for subtraction operation
    assert add_or_subtract(10, 4, '-') == 6
    assert add_or_subtract(-2, -5, '-') == 3
    assert add_or_subtract(8, -3, '-') == 11
    
    # Test for invalid operation
    assert add_or_subtract(5, 2, '*') == "Invalid operation. Use '+' or '-'"