import hello_world as hw
import math_operation as mo
import even_nums as en


hw.hello_world()                    # First task.

try:                                # Second task.
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    operation = input("Enter the operation (add, sub, mult, div):")
    try:
        print("Result is ", mo.calculate(a, b, operation))
    except Exception as err:
        print(err)
except Exception as err:
    print(err)

lst = list(range(1, 20))            # Third task.
print(en.even_nums(lst))