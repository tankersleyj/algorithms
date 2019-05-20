# MIT (c) jtankersley 2019-05-19
import unittest
from src import arg


class TestArg(unittest.TestCase):

    def test_arg_CommandHandler(self):
        print("test arg CommandHandler")
        cmd = arg.CommandHandler()
        self.assertEqual(cmd.is_command('discover'), True, "is_command")
        self.assertEqual(cmd._commands, ['discover'], "_commands")
        self.assertEqual(cmd.is_handled(), True, "is_handled")
        self.assertEqual(
            cmd.get_help(), "  commands: ['discover']\r\n", "get_help")
