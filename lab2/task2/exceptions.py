class UserError(Exception):
    def __str__(self):
        return "User wasn't set."


class OperandError(Exception):
    def __str__(self):
        return "Operands not found."
