from hello_world import greeting
from math_operation import calculate
from even_nums import find_even


greeting()                       # First task.

try:                                # Second task.
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    operation = input("Enter the operation (add, sub, mult, div):")
    try:
        print("Result is ", calculate(a, b, operation))
    except Exception as err:
        print(err)
except Exception as err:
    print(err)

lst = list(range(1, 20))            # Third task.
print(find_even(lst))
