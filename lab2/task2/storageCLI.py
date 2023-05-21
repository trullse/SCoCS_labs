from storage import Storage
from constants import ADD, REMOVE, FIND, LIST, GREP, SAVE, LOAD, SWITCH, HELP, EXIT, COMMANDS_HELP
from exceptions import UserError, OperandError
from json import JSONDecodeError


class StorageCLI:
    storage: Storage

    def __init__(self):
        self.storage = Storage()

    def command_handler(self, command: str):
        operands = command.split()
        try:
            if operands[0] == ADD:
                self._add_handler(operands[1:])
            elif operands[0] == REMOVE:
                self._remove_handler(operands[1:])
            elif operands[0] == FIND:
                self._find_handler(operands[1:])
            elif operands[0] == LIST:
                self._list_handler(operands[1:])
            elif operands[0] == GREP:
                self._grep_handler(operands[1:])
            elif operands[0] == SWITCH:
                self._switch_handler(operands[1:])
            elif operands[0] == SAVE:
                self._save_handler(operands[1:])
            elif operands[0] == LOAD:
                self._load_handler(operands[1:])
            elif operands[0] == HELP:
                self._help_handler(operands[1:])
            elif operands[0] == EXIT:
                self._exit_handler(operands[1:])
                return False
            else:
                print("'{}' is not a command. Write 'help' to see the commands.".format(operands[0]))
        except IndexError:
            print("Command wasn't found.")
        except UserError:
            print("User wasn't selected. Register using 'switch'.")
        except OperandError:
            print("Incorrect operand(s).")
        except KeyError:
            print("The key wasn't found.")
        except FileNotFoundError:
            print("The file is not found.")
        except JSONDecodeError:
            print("The file is broken.")
        return True

    def _add_handler(self, operands):
        if len(operands) == 0:
            raise OperandError
        self.storage.add(operands)

    def _remove_handler(self, operands):
        if len(operands) != 1:
            raise OperandError
        self.storage.remove(operands[0])

    def _find_handler(self, operands):
        if len(operands) == 0:
            raise OperandError
        result = self.storage.find(operands)
        if len(result) != 0:
            print("Found keys:\n{}".format(result))
        else:
            print("No keys found.")

    def _list_handler(self, operands):
        if len(operands) != 0:
            raise OperandError
        print(self.storage.list())

    def _grep_handler(self, operands):
        if len(operands) != 1:
            raise OperandError
        result = self.storage.grep(operands[0])
        if len(result) != 0:
            print("Grep result:\n{}".format(result))
        else:
            print("No matches found.")

    def _switch_handler(self, operands):
        if len(operands) != 1:
            raise OperandError
        if self.storage.user_selected() and self.storage.container_has_changes():
            if self._get_choice("Do you want to save changes?"):
                self.storage.save_changes()
        self.storage.switch_user(operands[0])
        if not self.storage.file_is_empty(operands[0]) \
                and self._get_choice("Do you want to load the existing container?"):
            self.storage.load_container()

    def _save_handler(self, operands):
        if len(operands) != 0:
            raise OperandError
        self.storage.save_changes()

    def _load_handler(self, operands):
        if len(operands) != 0:
            raise OperandError
        self.storage.load_container()

    def _help_handler(self, operands):
        if len(operands) != 0:
            raise OperandError
        print("This is an interactive CLI program which plays the role of a storage for unique elements and support "
              "a list of the following commands:")
        indent = max(len(command[0]) for command in COMMANDS_HELP) + 5
        for command in COMMANDS_HELP:
            print("  {:{}s}{}".format(command[0], indent, command[1]))

    def _exit_handler(self, operands):
        if len(operands) != 0:
            raise OperandError
        if self.storage.user_selected() and self.storage.container_has_changes():
            if self._get_choice("Do you want to save changes?"):
                self.storage.save_changes()

    def _get_choice(self, message: str):
        print(message + " Y/n ")
        while True:
            answer = input()
            if answer == "Y" or answer == "y":
                return True
            elif answer == "N" or answer == "n":
                return False
            else:
                print("Unknown command. " + message + " Y/n ")
