__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-

class MyError(TypeError):
    pass
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise myError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
if __name__ == '__main__':
    print(my_abs(0))
    print(my_abs('a'))
