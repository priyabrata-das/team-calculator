
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Interactive Test
print("Addition result:", add(10, 5))
print("Subtraction result:", subtract(10, 5))
print("Multiplication result:", multiply(10, 5))
print("Division result:", divide(10, 5))