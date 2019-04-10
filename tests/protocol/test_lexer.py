from unittest import TestCase

from fuocore.protocol import Lexer, FuoSyntaxError


lexer = Lexer()


class TestLexer(TestCase):

    def test_bad_string(self):
        with self.assertRaises(FuoSyntaxError):
            list(lexer.tokenize("play 'h"))

    def test_bad_cmd_option_1(self):
        with self.assertRaises(FuoSyntaxError):
            list(lexer.tokenize("play ["))

    def test_bad_cmd_option_2(self):
        with self.assertRaises(FuoSyntaxError):
            list(lexer.tokenize("play [name"))

    def test_cmd_with_options(self):
        tokens = lexer.tokenize("play hay [album=miao]")
        self.assertEqual(next(tokens).value, 'play')
        self.assertEqual(next(tokens).value, 'hay')
        next(tokens)
        self.assertEqual(next(tokens).value, 'album')

    def test_cast_int_float_string(self):
        tokens = lexer.tokenize("1 1.5 'aha'")
        self.assertEqual(next(tokens).value, 1)
        self.assertEqual(next(tokens).value, 1.5)
        self.assertEqual(next(tokens).value, 'aha')
