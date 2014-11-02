__author__ = 'akshay'


class NorthAt(object):
    __northAt = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(NorthAt, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, northAt=None):
        if northAt is not None:
            self.__northAt = northAt

    def getNorthAt(self):
        return self.__northAt

    def setNorthAt(self, northAt):
        self.__northAt = northAt