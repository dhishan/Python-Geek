import functools


def decoratorwithargs(func=None,karg1=None):

    def myDecorator(func):
        '''
        This is the decorator
        '''
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print "I am from the decorator"
            print karg1
            if karg1:
                print " THis is the {0}".format(karg1)
            return func(*args,**kwargs)

        return wrapper

    if func and karg1 is None and callable(func):
        # called as @decorator
        return myDecorator(func)

    else:
        return myDecorator
        # called as @decorator(args)

    # but what if the decorator is called with function as the argument
    # Doomed!!!
    # Thats the reason the decorators are always called with keyword arguments


@decoratorwithargs
def printmyname(name):
    print "Hello {0}".format(name)


@decoratorwithargs(karg1="her name")
def printhername(name):
    print "Hi {0}".format(name)


# Ref http://thecodeship.com/patterns/guide-to-python-function-decorators/
