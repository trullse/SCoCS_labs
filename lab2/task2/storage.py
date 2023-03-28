import json
from re import search
from json import dump, load, JSONDecodeError
from exceptions import UserError, OperandError
from constants import SAVE_PATH


class Storage:
    __current_user: str
    __current_container: set

    def __init__(self):
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

    def remove(self, key):
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
        if not self.user_selected():
            raise UserError
        with open(SAVE_PATH + self.__current_user + ".json", "r") as f:
            self.__current_container.update(load(f))

    def switch_user(self, username: str):
        self.__current_user = username
        self.__current_container = set()

    def save_changes(self):
        if not self.user_selected():
            raise UserError
        with open(SAVE_PATH + self.__current_user + ".json", "w") as f:
            dump(list(self.__current_container), f)

    def user_selected(self):
        if len(self.__current_user) == 0:
            return False
        else:
            return True

    def file_is_empty(self, container_name):
        try:
            with open(SAVE_PATH + container_name + ".json") as f:
                if len(load(f)) == 0:
                    return True
                else:
                    return False
        except FileNotFoundError:
            return True
        except JSONDecodeError:
            return False

    def container_has_changes(self):
        if not self.user_selected():
            raise UserError
        try:
            with open(SAVE_PATH + self.__current_user + ".json", "r") as f:
                if self.__current_container == set(load(f)):
                    return False
                else:
                    return True
        except (FileNotFoundError, json.JSONDecodeError):
            return True
