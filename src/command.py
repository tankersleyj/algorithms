# MIT, jtankersley, 2019-05-18
import sys

class Command():
  def __init__(self):
    # print(f"args: {sys.argv[1:]}")
    self._commands = []
    self._command = ""

  def arg(self, n, default_value):
    if len(sys.argv) > n:
      return sys.argv[n]
    else:
      return default_value
        
  def equal(self, command):
    if not command in self._commands:
      self._commands.append(command)
    if len(sys.argv) > 1:
      if command == sys.argv[1]:
        self._command = command
        return True
  
  def command(self):
    return self._command
  
  def commands(self):
    return self._commands

  def get_help(self, run_text='./run.sh'):
    print(f"  options: {self.commands()}")
    print(f"  example: {run_text} get_factors 40302")
