from src.pre_built.counter import count_ocurrences
from unittest.mock import patch, mock_open


def test_counter():
    # Ao ser chamada no 'assert', a count_ocurrences irá receber este mock
    mock = "Simple is better than complex. Complex is better than complicated."

    with patch('builtins.open', mock_open(read_data=mock)):
        # A palavra 'simple' aparece 1 vez na frase da variável 'mock'
        assert count_ocurrences('data/jobs.csv', 'simple') == 1

        # A palavra 'complex' aparece 2 vezes na frase da variável 'mock'
        assert count_ocurrences('data/jobs.csv', 'complex') == 2
