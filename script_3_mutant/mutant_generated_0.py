def add_or_subtract(a, b, operation):
    if operation == '+':
        return a * b
    elif operation == '-':
        return a - b
    else:
        return "Invalid operation. Use '+' or '-'"
