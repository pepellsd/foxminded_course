import pytest
from project import amount_of_unique_char


@pytest.mark.parametrize('input_str, expected', [("adadgggf", (1, ['f'])),
                                                 ("hjjjdhdfjs", (2, ['f', 's'])),
                                                 ("lnlnl", (0, [])),
                                                 ("qwert", (5, ['q', 'w', 'e', 'r', 't']))])
def test_return(input_str, expected):
    assert (amount_of_unique_char(input_str) == expected)


@pytest.mark.parametrize('input_type, exception', [(1, TypeError),
                                                   ([1, 23], TypeError)])
def test_input_type(input_type, exception):
    with pytest.raises(TypeError):
        assert amount_of_unique_char(input_type) == exception


if __name__ == "__main__":
    pytest.main()
