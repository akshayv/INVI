import subprocess
import threading
from integration.terminal.Platform import Platform

__author__ = 'raghav'


class CommandExecutor:
    def executeCommandWithOutput(self, commandString):
        if Platform().getOS() == "OS X":
            return subprocess.Popen(commandString, stdout=subprocess.PIPE).communicate()[0]
        elif Platform().getOS() == "Linux":
            pass

    # def __init__(self, cmd):
    #     self.cmd = cmd
    #     self.process = None
    #
    # def run(self, timeout):
    #     def target():
    #         print "Thread started"
    #         self.process = subprocess.Popen(self.cmd, shell=True)
    #         self.process.communicate()
    #         print "Thread finished"
    #
    #     thread = threading.Thread(target=target)
    #     thread.start()
    #
    #     thread.join(timeout)
    #     if thread.is_alive():
    #         print "Terminating process"
    #         self.process.terminate()
    #         thread.join()
    #     print self.process.returncode


if __name__ == "__main__":
    command_executor = CommandExecutor()
    print command_executor.executeCommandWithOutput(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-sNUS'])
    # print command_executor.executeCommand('ping google.com')
    # command = CommandExecutor("echo 'Process started'; sleep 2; echo 'Process finished'")
    # command.run(timeout=3)
    # command.run(timeout=1)