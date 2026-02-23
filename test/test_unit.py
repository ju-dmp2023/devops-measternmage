import pytest
from BE.calculator_helper import CalculatorHelper

class BaseTest:
    def setup_method(self):
        self.calc = CalculatorHelper()

    def teardown_method(self):
        del self.calc

class TestUnit(BaseTest):

    def test_add(self):
        result = self.calc.add(10, 5)
        assert result == 15

    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 6),
        (5, -5, 0),
        (10, 2, 12)
    ])
    def test_add_parameterized(self, a, b, expected):
        assert self.calc.add(a, b) == expected

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(10, 0)