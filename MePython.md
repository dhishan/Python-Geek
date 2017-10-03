## Inbuilts

chr(i) - inbuilt functions for ascii charracters
map(function,[iter]...) - maps the function through each element of the iterator
zip(a-iter,b-iter) - zips / maps each of the a to each of the b in order

Ex:
chrs = map(chr,range(97,104))
dchs = dict(zip(chrs,[1 for x in range(7)]))
out: dict of 7 charracters with values = 1\

() - creates an generator object without reset
{} - creates a dict object python > 3
[] - list


p = namedtuple('tuplename','a b c')
![](http://imgur.com/bvn3P6c)

Ordered Dict
![](http://imgur.com/7nvyU2T)

default dict val:
dict.get('',default val) or by using KeyError
import defaultdict from collections
dd = defaultdict(defval)

## Imports

from xx import *
all public imports or modules specifed by __all__ = ['funcname']

from .. import x
or
from ... import y

complex imports - pg 54

## Functions

### Keyword arguments:

```python3
>>>def func(opt):
...    print(opt)
>>>func(opt=1)
1
```

### Multiple Arguments

```python
>>>def func2(man, *varargs, opt=1, **varkeyargs):
...    print(man)
...    print(opt)
...    print(varargs)
...    print(varkeyargs)
>>> func2('dhishan','d','h',name='me')
dhishan
1
('d', 'h')
{'name':'me'}
>>> func2('something','ww','e',opt=5,att1='this')
something
5
('ww', 'e')
{'att1': 'this'}
```

Anything after the *args should be a keyword argument

## Classes

In python, everything is an object.
So the classes after being defined, become objects
So whats the class of the class object? Its python built in type() - which is the metaclass

- Class object
  classnamespace.attribute

- Instance object
  self.attribute it doesnt has to be self, its the first argument in the definition

- Method object or Instance method
  Functions in the python classes.
  x= Account()
  x.method() is equal to Account.method(x)

- Class Method
  created using @staticmethod or @classmethod

### Descriptor
Simply put, a descriptor is an object that represents the value of an attribute.A descriptor is any object that implements any of the __get__, __set__ or __delete__ special methods of the descriptor protocol. 
