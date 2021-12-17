import fibo

class TestFibo:
    def test_zero(self):
        assert fibo.fib(0) == 0

    def test_one(self):
        assert fibo.fib(1) == 1

    def test_ten(self):
        assert fibo.fib(10) == 55
