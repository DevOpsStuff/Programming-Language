#!/usr/bin/env python3

# with statement
"""
with open('hello.txt','w') as f:
    f.write('hello,world!')
"""
# Nothing much right, Opening files in a `with` statement is recomemded
# Because whenever you open files, you are supposed to close the file.

"""
This is what above code does using with statement
f = open('hello.txt','w')
try:
    f.write('hello,world')
finally:
    f.close()
"""
"""
What is Context Managers? 

It is a simple "protocol" that your objects needs to follow in order to 
support with statement. All you need to do is add `__enter__` and `__exit__` methods to an object if you
want it to function as a context Manager.

Take the below Example,

Class MyOpen:
     def __init__(self, name):
         self.name = name

    def __enter__(self):
        self.file = open(self.name,'w')
        return self.file
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.file:
            self.file.close()

with MyOpen('hello.txt') as f:
    f.write('helloworld')

"""

# The above approach is more of a class based approach
# lets use another approch using `contextlib`

"""
from contextlib import contextmanger

@contextmanager
def MyOpen(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with MyOpen('hello.txt') as f:
    f.write('hello world')
"""




