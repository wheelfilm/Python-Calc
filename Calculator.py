#----------------------------
# Python Test Calculator!!! -
# Created by Austin Wheeler -
# austnwheel@gmail.com      -
#----------------------------
print("Welcome to Python-Calc!")
print("This calculator is still a work in progress, so please be nice.")

def add(x, y):
    """Add the two given values!"""
    return x + y
def subtract(x, y):
    """Subtract the two given values!"""
    return x - y
def multiply(x, y):
    """Multiply the two given values!"""
    return x * y
def divide(x, y):
    """Divide the two given values!"""
    return x / y

x = int(input("Input your first number: "))

print("Input the number for your desired operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
op = str(input("1/2/3/4: "))

y = int(input("Input your second number: "))

if op == '1':
    result = add(x, y)
    print x, "plus", y, "=", result
elif op == '2':
    result = subtract(x, y)
    print x, "minus", y, "=", result
elif op == '3':
    result = multiply(x, y)
    print x, "times", y, "=", result
elif op == '4':
    result = divide(x, y)
    print x, "divided by", y, "=", result

print("With love,")
print("~Wheels <3")
