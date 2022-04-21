
from collections import namedtuple

qtystu = int(input().strip())
lstattr = list(input().split())
Student = namedtuple('Student', lstattr)
total = 0

for i in range(qtystu):
    lstvals = list(input().split())
    currstu = Student(lstvals[0], lstvals[1], lstvals[2], lstvals[3])
    total += int(currstu.MARKS)

print('{:.2f}'.format(total/qtystu))