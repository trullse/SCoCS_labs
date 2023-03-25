from storage import Storage
from constants import ADD, REMOVE, FIND, LIST, GREP, SAVE, LOAD, SWITCH


class StorageCLI:
    storage: Storage

    def __init__(self):
        self.storage = Storage()

    def command_handler(self, command: str):
        operands = command.split()
        if operands[0] == ADD:
            operands = operands[1:]
            self.add_handler(operands)
        elif operands[0] == SWITCH:
            operands = operands[1:]
            self.switch_handler(operands)

    def add_handler(self, operands):
        try:
            self.storage.add(operands)
        except AttributeError:
            print("User wasn't selected. Register using 'switch'.")

    def switch_handler(self, operands):
        pass
