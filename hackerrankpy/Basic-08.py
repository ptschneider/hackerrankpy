#!/bin/python3
from collections import OrderedDict

od = {}
qtyitems = int(input().strip())
for i in range(qtyitems):
    item, price = input().rsplit(' ', 1)
    od[item] = od.get(item, 0) + int(price)
print(*[" ".join([item, str(price)]) for item, price in od.items()], sep="\n")
