'''
for reference only: type sizes in python

'''

#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Goal: To examine which type is the smallest in Python
Types used: int, float, str, list, tuple, dict, set, frozenset
            None, Ellipsis, object, lambda, function, Exception
"""
def f(): return

types = [int(0), float(0), str(), list(), tuple(), dict(), set(), frozenset(),
         None, ..., object(), lambda: None, f, Exception()]

names = ["int", "float", "str", "list", "tuple", "dict", "set", "frozenset",
         "None", "Ellipsis", "Object", "Lambda", "Function-ref", "Exception"]

sizes = list(map(lambda x: x.__sizeof__(), types))

for t, s in zip(names, sizes):
    print("Size of {} is: {}".format(t, s))


"""
Output:
Size of int is: 24
Size of float is: 24
Size of str is: 49
Size of list is: 40
Size of tuple is: 24
Size of dict is: 264
Size of set is: 200
Size of frozenset is: 200
Size of None is: 16
Size of Ellipsis is: 16
Size of Object is: 16
Size of Lambda is: 112
Size of Function-ref is: 112
Size of Exception is: 64
It seems None, Ellipsis and Object are very similar
Fun experiment: replace all instances of None with ...
"""
