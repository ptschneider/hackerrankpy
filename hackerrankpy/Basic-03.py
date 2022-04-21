#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

deq = deque()
c = int(input())
for i in range(c):
    lst = list(map(str, input().split()))
    m = lst[0]
    if len(lst) > 1:
        n = int(lst[1])
    if m == "append":
        deq.append(n)
    elif m == "appendleft":
        deq.appendleft(n)
    elif m == "pop":
        deq.pop()
    elif m == "popleft":
        deq.popleft()

print(*deq)
