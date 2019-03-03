import pytest
from unittest import mock
from clean.calc import Calc


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 9


def test_add_three_numbers():
    c = Calc()

    res = c.add(4, 5, 6)

    assert res == 15


def test_add_hundred_numbers():
    c = Calc()

    s = range(100)

    assert c.add(*s) == 4950


def test_subtract_two_numbers():
    c = Calc()

    res = c.sub(10, 3)

    assert res == 7


def test_multiply_two_numbers():
    c = Calc()

    res = c.mul(5, 3)

    assert res == 15


def test_multiply_three_numbers():
    c = Calc()

    res = c.mul(3, 5, 4)

    assert res == 60


def test_multiply_ten_numbers():
    c = Calc()

    s = range(1, 10)

    res = c.mul(*s)

    assert res == 362880


def test_divide_two_numbers_float():
    c = Calc()

    res = c.div(13, 2)

    assert res == 6.5


def test_divide_other_two_numbers():
    c = Calc()

    res = c.div(9, 2)

    assert res == 4.5


def test_div_by_zero_returns_inf():
    c = Calc()

    res = c.div(99, 0)

    assert res == 'inf'


def test_mul_by_zero_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.mul(9, 0)


def test_avg_correct_average():
    c = Calc()

    res = c.avg([2, 5, 12, 98])

    assert res == 29.25


def test_avg_removes_upper_outliers():
    c = Calc()

    res = c.avg([3, 3, 4, 98, 101], upper=10)

    assert res == pytest.approx(3.333333)


def test_avg_removes_lower_outliers():
    c = Calc()

    res = c.avg([1, 3, 3, 4], lower=2)

    assert res == pytest.approx(3.333333)


def test_avg_removes_upper_outlier_at_border():
    c = Calc()

    res = c.avg([3, 3, 4, 5], upper=5)

    assert res == pytest.approx(3.333333)


def test_avg_removes_lower_outlier_at_border():
    c = Calc()

    res = c.avg([2, 3, 3, 4], lower=2)

    assert res == pytest.approx(3.333333)


def test_avg_removes_with_both_bounds():
    c = Calc()

    res = c.avg([2, 3, 3, 4, 5], lower=2, upper=5)

    assert res == pytest.approx(3.333333)


def test_avg_returns_zero_for_empty_list():
    c = Calc()

    res = c.avg([])

    assert res == 0


def test_avg_returns_zero_after_filterd_list_is_empty():
    c = Calc()

    res = c.avg([1, 2, 3], lower=2, upper=3)

    assert res == 0


def test_can_connect_to_mock():
    external_obj = mock.Mock()
    c = Calc(external_obj)
    external_obj.connect.assert_called_with()