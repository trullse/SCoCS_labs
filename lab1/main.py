import hello_world as hw
import math_operation as mo
import even_nums as en


hw.hello_world()                    # First task.

print("Enter the first number:")    # Second task.
a = input()
print("Enter the second number:")
b = input()
print("Enter the operation (add, sub, mult, div):")
operation = input()
try:
    print("Result is ", mo.do_operation(a, b, operation))
except Exception as err:
    print(err)

lst = list(range(1, 20))            # Third task.
print(en.even_nums(lst))