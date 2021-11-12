from project import cli, format_return, work_with_args
import unittest
from unittest.mock import MagicMock, patch, mock_open


class TestCLI(unittest.TestCase):
    def test_cli(self):
        parser = cli(args=["--string", "lskflksd", "--file", "B:/test.txt"])
        self.assertEqual(parser.string, "lskflksd")
        self.assertEqual(parser.file, "B:/test.txt")

    def test_file_error(self):
        mock_file = MagicMock(return_value='C:/somefile.txt')
        with self.assertRaises(FileNotFoundError) as e:
            self.assertEqual(work_with_args(file=mock_file.return_value, string=""), e.exception.args[0])

    def test_format_return(self):
        self.assertEqual(format_return('jkshdkjfa'), '"jkshdkjfa" => 5\ns,h,d,f,a are present once.')
        self.assertEqual(format_return('jjgghh'), '"jjgghh" => 0\nnone are present once.')

    def test_return_args_string(self):
        self.assertEqual(work_with_args(file='', string="jskl"), "jskl")

    def test_return_args_file(self):
        with patch("builtins.open", mock_open(read_data="sdjkfhskjd\ndhfk")) as mock_file:
            open("path/to/open").read()
            mock_file.assert_called_with("path/to/open")
            self.assertEqual(work_with_args(file=mock_file, string=''), "sdjkfhskjddhfk")


if __name__ == "__main__":
    unittest.main()