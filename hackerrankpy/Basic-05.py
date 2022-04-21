#!/bin/python3
from collections import Counter

qtyshoes = int(input().strip())
# print(" ")
# print("qtyshoes " + str(qtyshoes))

lstsize = list(map(int, input().split()))
# print("lstsize " + str(len(lstsize)))
# print("*listsize " + str(lstsize))
cntrsize = Counter(lstsize)

qtycust = int(input().strip())
# print("qtycust " + str(qtycust))

total = 0
onhand = 0
for i in range(qtycust):
    size, price = map(int, input().split())
    if cntrsize[size] > 0:
        cntrsize[size] -= 1
        total += price

print(str(total))
