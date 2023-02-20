from constants import ADD, SUB, MULT, DIV


def do_operation(x, y, oper):
    x = float(x)
    y = float(y)

    if oper == ADD:
        return x + y
    elif oper == SUB:
        return x - y
    elif oper == MULT:
        return x * y
    elif oper == DIV:
        return x / y

    raise Exception("Operation is not implemented!")