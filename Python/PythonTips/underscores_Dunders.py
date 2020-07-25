"""
UnderScores:

1) Single UNderscores: _var

It is more of a indication to the Python Programmers, a kind of private variable
But doesn't enforce it.

class Test:
    def __init__(slef):
        self.foo = 11
        self._bar = 23

t = Test()
print(t.foo)
print(t._bar)

# my_module
def external():
    return 23

def _internal():
    pass

from my_module import *
external()
prints 23
_internal()
NameError Not defined

Note: WildCard imports should be avoided

2) Single Trailing Underscore: "var_"

Sometimes for the NameConvention we use the words like, 
len,class,string

use trialing characters

len_ = len(a)

def make_object(name,class): #Invalid Syntax

def make_object(name,class_): # Valid Syntax

3) Double Leading Underscore: "__var"

class Test:
    def __init__(self):
        self.foo = 1
        self._bar = 2
        self.__bax = 3

>>> t = Test()
>>> dir(t)
['_Test__bax', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']
>>>

Hope You have noticed something from the output. Interstingly you might seen this two variables
self.foo = 1
self._bar = 2
but, also this, '_Test__bax' -> is called 'Name Managling'

class ExtentedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__bax = 'overridden'

>>> t2 = ExtentedTest()
>>> t2.foo
'overridden'
>>> t2._bar
'overridden'
>>> t2.__baz
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ExtentedTest' object has no attribute '__baz'

This is called Name Managling

>>> dir(t2)
['_ExtentedTest__bax', '_Test__bax', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']

>>> t2._ExtentedTest__bax
'overridden'
>>> t2._Test__bax
3

Dunders

Anything thats starts and ends with __
like, __init__ 

4) single Underscore: _

means "Dont Care"

>>> a = [random.randint(1,10)] * 10
>>> a
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
for _,v in enumerate(a):
    print(v)

"""
