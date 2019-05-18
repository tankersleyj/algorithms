# MIT, jtankersley, 2019-05-18
import sys


def get_arg(n, default_value):
  if len(sys.argv) > n:
    return sys.argv[n]
  else:
    return default_value


def is_equal(n, command):
  result = False
  if len(sys.argv) > n:
    if command == sys.argv[n]:
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
    if not command in self._commands:
      self._commands.append(command)
    if is_equal(1, command):
      self._command = command
      return True
    else:
      return False
  
  def is_handled(self):
    if self._command in self._commands:
      return True
    else:
      return False

  def get_help(self, title="", options=[], run_text='./run.sh'):
    if len(title) > 0:
      print(title)
    if len(options) == 0:
      options = self._commands
    if len(options) > 0:
      print(f"  options: {self._commands}")
    print(f"  example: {run_text} get_factors 40302")
