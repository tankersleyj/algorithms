# MIT (c) jtankersley 2019-05-19
import unittest
from src import arg

class TestArg(unittest.TestCase):

  def test_(self):
      print("test arg")
      self.assertGreater(len(arg.get_args()), 0, "get_args")
      self.assertEqual(arg.get_arg(1), 'discover', "get_arg(1)")
      cmd = arg.CommandHandler()
      self.assertEqual(cmd.is_command('discover'), True, "is_command")
      self.assertEqual(cmd._commands, ['discover'], "_commands")
      self.assertEqual(cmd.is_handled(), True, "is_handled")
      self.assertEqual(cmd.get_help(), "  commands: ['discover']\n", "get_help")
