#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ziyi'

# file two.py
import one        # start executing one.py

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

'这下终于清静了不少' \
'分支的内容先add再commit没有必要push'