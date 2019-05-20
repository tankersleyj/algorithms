#  MIT (c) jtankersley 2019-05-19
import unittest
from src import args


class TestArgs(unittest.TestCase):

    def test_args_CommandHandler(self):
        print("test args CommandHandler")
        cmd = args.CommandHandler()
        self.assertEqual(cmd.is_command('discover'), True, "is_command")
        self.assertEqual(cmd._commands, ['discover'], "_commands")
        self.assertEqual(cmd.is_handled(), True, "is_handled")
        self.assertEqual(
            cmd.get_help(), "  commands: ['discover']\r\n", "get_help")
