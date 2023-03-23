from re import search


class Storage:
    __storage: set

    def __init__(self):
        self.__storage = set()

    def add(self, key):
        if isinstance(key, str):
            self.__storage.add(key)
        elif isinstance(key, list):
            self.__storage.update(key)

    def contains(self, key):
        return key in self.__storage

    def remove(self, key):          # use try .. catch
        self.__storage.remove(key)

    def find(self, key):
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
        return list(self.__storage)

    def grep(self, regex):
        grep_result = list()
        for key in self.__storage:
            if search(regex, key) is not None:
                grep_result.append(key)
        return grep_result
