from collections import deque

qtytests = int(input().strip())
processing = False
stackable = False
ablx = deque()
for j in range(qtytests):
    qtyqubs = map(int, input().strip())
    ablx.append(deque(map(str, input().split())))

for k in range(len(ablx)):
    blx = ablx.popleft()
    last = -1
    if len(blx) < 3:
        processing = False
        stackable = True
    else:
        processing = True
        stackable = False

    while processing:
        if last == -1:
            if blx[0] >= blx[-1]:
                last = blx.popleft()
            else:
                last = blx.pop()
        else:
            if last >= blx[0]:
                if len(blx) > 1:
                    if blx[-1] > last:
                        stackable = False
                        processing = False
                    else:
                        if blx[-1] > blx[0]:
                            last = blx.pop()
                        else:
                            last = blx.popleft()
                else:
                    last = blx.popleft()

                if len(blx) < 1:
                    stackable = True
                    processing = False
            else:
                stackable = False
                processing = False

    if stackable:
        print("Yes")
    else:
        print("No")

# blx = deque(map(str, input().split()))
# last = -1
# if len(blx) < 3:
#     print("Yes")
# processing = True
# stackable = False
# while processing:
#     if last == -1:
#         if blx[0] > blx[-1]:
#             last = blx.popleft()
#         else:
#             last = blx.pop()
#     else:
#         if (last < blx[0]) & (last < blx[-1]):
#             if blx[0] > blx[-1]:
#                 last = blx.popleft()
#             else:
#                 last = blx.pop()
#             if len(blx) < 1:
#                 stackable = True
#         else:
#             stackable = False
#             break
#
# if stackable:
#     print("Yes")
# else:
#     print("No")

# print("len(blx) " + str(len(blx)))
# print("blx[0] " + blx[0])
# print("blx[-1] " + blx[-1])
# print("blx[len(blx)-1] " + blx[len(blx)-1])
# print("blx.pop()" + str(blx.pop()))
# print("blx.popleft()" + str(blx.popleft()))

# vblx = deque()
# if len(blx) < 3:
#     print("Yes")
# else:
#     processing = True
#     while processing:
#         l = blx.popleft()
#         r = blx.pop()
#         if r > l:
#             vblx.append(r)
#             last = r
#             blx.appendleft(l)
#         else:
#             vblx.append(l)
#             last = l
#             blx.append(r)

#print(*blx)