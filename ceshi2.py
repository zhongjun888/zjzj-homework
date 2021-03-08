# coding=utf-8
import pytest
from ceshi3 import Calculator


class TestCal:
    def setup_method(self):
        self.cal = Calculator()
        print("开始计算")
    def teardown_method(self):
        print("结束计算\n")

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 8), (-1, -2, -3), (300, 500, 800)], ids= ["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        print("%d + %d = %d" %(a, b, expect))
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, expect", [(8, 2, 6), (-1, 2, -3), (300, 100, 200)], ids= ["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        print("%d - %d = %d" %(a, b, expect))
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 15), (-1, -2, 2), (300, 50, 15000)], ids= ["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        print("%d * %d = %d" %(a, b, expect))
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", [(8, 2, 4), (-8, -2, 4), (300, 2, 150)], ids= ["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        print("%d / %d = %d" %(a, b, expect))
        assert expect == self.cal.div(a, b)