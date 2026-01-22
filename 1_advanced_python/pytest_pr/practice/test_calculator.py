import pytest
from calculator import Calculator
from contextlib import nullcontext as no_raise

class TestCalculator:

    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (1, 2, 3, no_raise()),
            (3, 10, 13, no_raise()),
            ('5', 2, 7, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, a, b, res, expectation):
        with expectation:
            assert Calculator().add(a, b) == res


    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (1, 2, -1, no_raise()),
            (13, 10, 3, no_raise()),
            (-1, -2, 1, no_raise()),
            ('-1', -2, 1, pytest.raises(TypeError)),
            (-1, '-2', 1, pytest.raises(TypeError)),
            (-1, -2, 0, pytest.raises(AssertionError)),
        ]
    )
    def test_sub(self, a, b, res, expectation):
        with expectation:
            assert Calculator().subtract(a, b) == res


    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (1, 2, 2, no_raise()),
            (13, 10, 130, no_raise()),
            (-1, -2, 2, no_raise()),
            ('-1', -2, 1, pytest.raises(TypeError)),
            (-1, '-2', 1, pytest.raises(TypeError)),
            (-1, -2, '1', pytest.raises(AssertionError)),
            (-1, -2, 0, pytest.raises(AssertionError)),
        ]
    )
    def test_mult(self, a, b, res, expectation):
        with expectation:
            assert Calculator().multiply(a, b) == res


    @pytest.mark.parametrize(
        "a, b, res, expectation",
        [
            (1, 2, 0.5, no_raise()),
            (13, 10, 13/10, no_raise()),
            (-1, -2, 0.5, no_raise()),
            ('-1', -2, 1, pytest.raises(TypeError)),
            (-1, '-2', 1, pytest.raises(TypeError)),
            (-1, -2, '1', pytest.raises(AssertionError)),
            (-1, -2, 0, pytest.raises(AssertionError)),
            (-1, 0, 0, pytest.raises(ValueError)),
            # (-1, 0, 0, pytest.raises(ZeroDivisionError)) after changing func logic 23-24 lines,
        ]
    )
    def test_div(self, a, b, res, expectation):
        with expectation:
            assert Calculator().divide(a, b) == res

