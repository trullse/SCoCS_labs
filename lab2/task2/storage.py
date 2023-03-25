from re import search
from exceptions import UserError


class Storage:
    __storage: dict
    __current_user: str
    __current_container: set

    def __init__(self):
        self.__storage = dict()

    def add(self, key):
        if self.__current_user is None:
            raise UserError
        if isinstance(key, str):
            self.__current_container.add(key)
        elif isinstance(key, list):
            self.__current_container.update(key)

    def contains(self,  key):
        if self.__current_user is None:
            raise UserError
        return key in self.__current_container

    def remove(self, key):          # use try .. catch
        if self.__current_user is None:
            raise UserError
        self.__current_container.remove(key)

    def find(self, key):
        if self.__current_user is None:
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
        if self.__current_user is None:
            raise UserError
        return list(self.__current_container)

    def grep(self, regex):
        if self.__current_user is None:
            raise UserError
        grep_result = list()
        for key in self.__current_container:
            if search(regex, key) is not None:
                grep_result.append(key)
        return grep_result

    def load_container(self):
        if self.__current_user is None:
            raise UserError
        if self.__storage[self.__current_user] is None:
            self.__storage[self.__current_user] = set()
        if len(self.__current_container) == 0:
            self.__current_container = self.__storage[self.__current_user].copy()
        if len(self.__current_container) != 0:
            self.__current_container.update(self.__storage[self.__current_user])

    def switch_user(self, username: str):
        self.__current_user = username
        self.__current_container = set()

    def save_changes(self):
        if self.__current_user is None:
            raise UserError
        self.__storage[self.__current_user] = self.__current_container
