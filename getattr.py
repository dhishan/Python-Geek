
class A(object):

    def __init__(self):
        pass

    def printer(self,input):
        print(input)

    def __getattr__(self,atr):
        print("incoming")
        if atr == 'methd':
            return self.printer
