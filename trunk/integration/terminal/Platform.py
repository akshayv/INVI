from sys import platform as _platform

__author__ = 'raghav'

class Platform:
    @staticmethod
    def getOS():
        operating_system = None
        if _platform == "darwin":
            operating_system = "OS X"
        elif _platform == "linux" or _platform == "linux2":
            operating_system = "Linux"
        elif _platform == "win32":
            operating_system = "Windows"
        return operating_system

