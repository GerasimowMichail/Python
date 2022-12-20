import pytest
from my_funcs import my_sum, my_div, my_sequence

@pytest.mark.parametrize('x, y, expected_result', [(5, 2, 7), (4, 3, 7), (5, 0, 5)])
def test_my_sum_good(x, y, expected_result):
    assert my_sum(x, y) == expected_result


list_example = [(15, 3, 5.0), (4, 2, 2.0), (5, 1, 5.0)]
@pytest.mark.parametrize('x, y, expected_result', list_example)
def test_my_div_good(x, y, expected_result):
    assert my_div(x, y) == expected_result

list_example_err = [(5, 0, ZeroDivisionError), (5, '2', TypeError)]
@pytest.mark.parametrize('x, y, expected_exception', list_example_err)
def test_my_div_with_err(x, y, expected_exception):
    with pytest.raises(expected_exception):
        my_div(x, y)

# test_
list_example = [(2, [3, 9]), (3, [3, 9, 27]), (4, [3, 9, 27, 81]), (5, [3, 9, 27, 81, 243])]
@pytest.mark.parametrize('a, z', list_example)
def test_my_sequence_good(a, z):
    assert my_sequence(a) == z

# запуск теста из командной строки:
# python -m pytest -v test_my_funcs.py