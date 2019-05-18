# MIT, jtankersley, 2019-05-18
import sys


def get_arg(n, default):
  if len(sys.argv) > n:
    return sys.argv[n]
  else:
    return default


def is_arg(n, value):
  result = False
  if len(sys.argv) > n:
    if value == sys.argv[n]:
      return True
  return result


class CommandHandler():
  # opinionated class methods using non-opinionated functions

  def __init__(self):
    self._commands = []
    self._command = ""

  def arg(self, n, default_value):
    return get_arg(n, default_value)
        
  def equal(self, command):
    # defines argument[1] as a command
    if not command in self._commands:
      self._commands.append(command)
    if is_arg(1, command):
      self._command = command
      return True
    else:
      return False
  
  def is_handled(self):
    if self._command in self._commands:
      return True
    else:
      return False

  def get_help(self, title="", example="", options=[]):
    if len(title) > 0:
      print(title)
    if len(options) == 0:
      options = self._commands
    if len(example) > 0:
      print(f"  example: {example}")
    if len(options) > 0:
      print(f"  options: {self._commands}")
