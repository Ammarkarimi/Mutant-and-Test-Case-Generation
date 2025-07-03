def add_or_subtract(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    else:
        return "Invalid operation. Use '+' or '-'"


def test():
    # Test addition
    assert add_or_subtract(2, 3, '+') == 5
    assert add_or_subtract(10, 5, '+') == 15
    
    # Test subtraction
    assert add_or_subtract(8, 4, '-') == 4
    assert add_or_subtract(100, 20, '-') == 80
    
    # Test invalid operation
    assert add_or_subtract(5, 3, '*') == "Invalid operation. Use '+' or '-'"