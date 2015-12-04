#!/usr/bin/env python
import hashlib
from inputs import day4 as secret_key

m = hashlib.md5()

found_5 = False
found_6 = False

for i in range(100000000):
    val = hashlib.md5(secret_key+str(i)).hexdigest()
    if not found_5 and val.startswith('00000'):
        found_5 = True
        print("{} starts with 5 zeros and was generated using int: {} ".format(val, i))
    if not found_6 and val.startswith('000000'):
        found_6 = True
        print("{} starts with 6 zeros and was generated using int: {} ".format(val, i))
    if found_5 and found_6:
        break
