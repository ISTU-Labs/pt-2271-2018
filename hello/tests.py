import euler
from models import Euler


class TestTest:

    def test_test(self):
        assert True

    def test_euler(self):
        rlen = euler.new_rlen()
        rc = euler.calculate(
            0.01,
            24.0,
            0.0,
            100.0,
            0.1,
            0.01,
            10,
            rlen
        )

        #for i in range(euler.get_len(rlen)):
        #    print(i,":", euler.get_i(rc, i))

        assert abs(euler.get_i(rc, 0)-100.0) < 0.001
        euler.release(rc)
        euler.release_rlen(rlen)

    def test_wrapper_class(self):
        e = Euler(
            0.01,
            24.0,
            0.0,
            100.0,
            0.1,
            0.01,
            10)
        e.calculate()
        assert abs(e[0]-100.0) < 0.001
