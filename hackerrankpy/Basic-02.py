#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input().strip())

od = OrderedDict()

for i in range(n):
    key = input()
    if key in od.keys():
        od[key] += 1
    else:
        od.update({key: 1})

print(len(od.keys()))
print(*od.values())
#print(od.values())

