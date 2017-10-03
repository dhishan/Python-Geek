from contextlib import contextmanager


@contextmanager
def lets_yield():
    print("In Yielder")
    try:
        yield
    finally:
        print("I am at finally ")


class Saved():

    def __init__(self, cr):
        self.cr = cr

    def __enter__(self):
        print("I am enter")
        return self.cr

    def __del__(self):
        del self.cr
        print("I deleted your object and myself")


class test():

    def __init__(self):
        self.iii()
        pass

    def iii(self):
        v = 1
        self.i = Saved(v)
