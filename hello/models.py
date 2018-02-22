import euler

class Euler(object):
    def __init__(self,
                 k,Tenv,
                 t0,T0,
                 h,eps,
                 m
    ):
        self.k=k
        self.Tenv=Tenv
        self.t0=t0
        self.T0=T0
        self.h=h
        self.eps=eps
        self.m=m
        self._rlen=euler.new_rlen()
        self._result=None

    def release_result(self):
        if self._result is not None:
            euler.release(self._result)
        self._result=None

    def __del__(self):
        self.release_result()
        euler.release_rlen(self._rlen)

    def calculate(self):
        self.release_result()
        self._result = euler.calculate(
            self.k, self.Tenv,
            self.t0, self.T0,
            self.h, self.eps,
            self.m,
            self._rlen
        )
        return self._result

    def __getitem__(self, index):
        assert self._result is not None, "run calculate method to get result"
        return euler.get_i(self._result, index)

