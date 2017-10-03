class PluginMount(type):
    """docstring for ."""
    def __init__(cls, name, bases, attrs):
        print(cls)
        if not hasattr(cls,'plugins'):
            cls.plugins = []
            print("This is from the plugin mounter")
        else:
            cls.plugins.append(cls)
        super(PluginMount, cls).__init__(name, bases, attrs)


class A(object,metaclass=PluginMount):
    """This is the base class: aka Plugin Mount - IMplement printer(input)"""
    def __init__(self):
        print("Printin from Class A")

    def printer(self,input):
        print(input)


class B(A):
    """docstring for ."""
    def __init__(self):
        super(B, self).__init__()
