from datetime import datetime
from unittest.mock import patch
from src.main import greet, main


class TestGreet:

    def test_greet(self):
        name = "Alice"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expected_output = f"Hello, {name}! Welcome to our program. Current time is {current_time}."

        result = greet(name)

        assert result == expected_output

    @patch('sys.argv', ['main.py', 'Bob'])
    @patch('builtins.print')
    def test_main_with_name_argument(self, mock_print):
        main()

        expected_output = greet('Bob')
        mock_print.assert_called_with(expected_output)
