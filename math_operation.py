def do_operation(x, y, oper):

    if oper == ADD:
        return x + y
    elif oper == SUB:
        return x - y
    elif oper == MULT:
        return x * y
    elif oper == DIV:
        return x / y

    raise Exception("Operation is not implemented!")
    