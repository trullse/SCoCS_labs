from re import search
from json import dump, load
from exceptions import UserError, OperandError


class Storage:
    __storage: dict
    __current_user: str
    __current_container: set

    def __init__(self):
        self.__storage = dict()
        self.__current_user = str()

    def add(self, key):
        if not self.user_selected():
            raise UserError
        if isinstance(key, str):
            self.__current_container.add(key)
        elif isinstance(key, list):
            if len(key) == 0:
                raise OperandError
            self.__current_container.update(key)

    def contains(self,  key):
        if not self.user_selected():
            raise UserError
        return key in self.__current_container

    def remove(self, key):          # use try .. catch
        if not self.user_selected():
            raise UserError
        self.__current_container.remove(key)

    def find(self, key):
        if not self.user_selected():
            raise UserError
        find_result = list()
        if isinstance(key, str):
            if self.contains(key):
                find_result.append(key)
        elif isinstance(key, list):
            for el in key:
                if self.contains(el):
                    find_result.append(el)
        return find_result

    def list(self):
        if not self.user_selected():
            raise UserError
        return list(self.__current_container)

    def grep(self, regex):
        if not self.user_selected():
            raise UserError
        grep_result = list()
        for key in self.__current_container:
            if search(regex, key) is not None:
                grep_result.append(key)
        return grep_result

    def load_container(self):
        if self.__current_user not in self.__storage:
            self.__storage[self.__current_user] = set()
        if len(self.__current_container) == 0:
            self.__current_container = self.__storage[self.__current_user].copy()
        if len(self.__current_container) != 0:
            self.__current_container.update(self.__storage[self.__current_user])

    def switch_user(self, username: str):
        self.__current_user = username
        self.__current_container = set()

    def save_changes(self):
        if not self.user_selected():
            raise UserError
        self.__storage[self.__current_user] = self.__current_container

    def save_to_file(self, path):
        with open(path, "w") as f:
            dump(list(self.__current_container), f)

    def load_from_file(self, path):
        with open(path, "r") as f:
            self.__current_container.update(load(f))

    def user_selected(self):
        if len(self.__current_user) == 0:
            return False
        else:
            return True

    def container_is_empty_or_none(self, container_name=None):
        if container_name is None:
            if self.user_selected() and len(self.__current_container) != 0:
                return False
            else:
                return True
        else:
            if container_name in self.__storage and len(self.__storage[container_name]) != 0:
                return False
            else:
                return True

    def container_has_changes(self):
        if not self.user_selected():
            raise UserError
        if self.__current_user in self.__storage and self.__current_container == self.__storage[self.__current_user]:
            return False
        return True
