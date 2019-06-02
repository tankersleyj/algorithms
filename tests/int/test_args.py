#  MIT (c) jtankersley 2019-05-19
import unittest
from src import args


class TestArgs(unittest.TestCase):

    def test_args_CommandHandler(self):
        cmd = args.CommandHandler()
        self.assertEqual(cmd.isCommand('discover'), True, "isCommand")
        self.assertEqual(cmd._commands, ['discover'], "_commands")
        self.assertEqual(cmd.isHandled(), True, "isHandled")
        self.assertEqual(
            cmd.getHelp(), "  commands: ['discover']\r\n", "getHelp")
