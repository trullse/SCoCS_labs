class UserError(Exception):
    def __str__(self):
        return "User wasn't set."
