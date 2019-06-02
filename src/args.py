#  MIT (c) jtankersley 2019-05-18
import sys


def getArg(n, default=None):
    if len(sys.argv) > n:
        return sys.argv[n]
    else:
        return default


def getArgs():
    return sys.argv


class CommandHandler():
    #  defines argument[1] as command consuming arguments[2:n]

    def __init__(self):
        self._commands = []
        self._command = ""

    def arg(self, n, default):
        return getArg(n, default)

    def isCommand(self, command):
        if command not in self._commands:
            self._commands.append(command)
        if getArg(1, "") == command:
            self._command = command
            return True
        else:
            return False

    def isHandled(self):
        if self._command in self._commands:
            return True
        else:
            return False

    def getHelp(self, title="", format="", example="", commands=[]):
        help_text = ""
        if len(title) > 0:
            help_text += f"{title}\n"
        if len(commands) == 0:
            commands = self._commands
        if len(format) > 0:
            help_text += f"  format: {format}\r\n"
        if len(example) > 0:
            help_text += f"  example: {example}\r\n"
        if len(commands) > 0:
            help_text += f"  commands: {self._commands}\r\n"
        return help_text
