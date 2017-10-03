class A(object):

    def __init__(self,val):
        self.r = val
        print("Class A")

    def prontfrmA(self):
        print("from A%s" % self.r)


class B(A):
    def __init__(self):
        print("Class B")

    def pront(self):
        self.prontfrmA()
