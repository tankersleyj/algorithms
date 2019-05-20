# MIT (c) jtankersley 2019-05-18
import sys


def get_arg(n, default=None):
    if len(sys.argv) > n:
        return sys.argv[n]
    else:
        return default


def get_args():
    return sys.argv


class CommandHandler():
    # defines argument[1] command consuming arguments[2:n]

    def __init__(self):
        self._commands = []
        self._command = ""

    def arg(self, n, default):
        return get_arg(n, default)

    def is_command(self, command):
        if command not in self._commands:
            self._commands.append(command)
        if get_arg(1, "") == command:
            self._command = command
            return True
        else:
            return False

    def is_handled(self):
        if self._command in self._commands:
            return True
        else:
            return False

    def get_help(self, title="", example="", commands=[]):
        help_text = ""
        if len(title) > 0:
            help_text += f"{title}\n"
        if len(commands) == 0:
            commands = self._commands
        if len(example) > 0:
            help_text += f"  example: {example}\r\n"
            # print(f"  example: {example}")
        if len(commands) > 0:
            # print(f"  commands: {self._commands}")
            help_text += f"  commands: {self._commands}\r\n"
        return help_text
