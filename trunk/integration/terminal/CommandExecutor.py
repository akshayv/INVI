import subprocess

__author__ = 'raghav'

class CommandExecutor:
    @staticmethod
    def executeCommand(commandString):
        output = subprocess.Popen(commandString, stdout=subprocess.PIPE).communicate()[0]
        return output
