"""
1) Old-Style

>>> name = "Tesla"
>>> 'hello, %s' % name
'hello, Tesla'

2) New Style

>>> 'hello, {}'.format(name)
'hello, Tesla'
>>>

3) f'strings (python3.6+)
4) Template String

>>> from string import Template
>>> t = Template('Hey, $name')
>>> t.substitute(name=name)
'Hey, Tesla'
>>>
"""
