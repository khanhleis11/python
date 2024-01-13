from math import *

# a, b = map(int, input().split())

# tmp = a // b
# print(tmp)
# res = floor(tmp)
# ans = tmp + 1
# print(ans)
# print(tmp * b, (tmp + 1) * b)

# 717 689

#kiem tra tam giac
# a, b, c = map(int, input().split())
# if (a + b < c and a + c < b and c + b < a and a > 0 and b > 0 and c > 0):
#     print("INVALID")
# else:
#     if (a == b or b == c or c == a):
#         if (a == b and b == c):
#             print(1)
#         else: print(2)
#     elif ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2)):
#         print(3)
#     else: print(4)

#ki tu ke tiep
s = input()
tmp = ord(s)
if s >= "A" and s < "Z":
    tmp += 33
elif s == "Z" or s == "Z":
    print("a")
s = chr(tmp)
print(s)

# isupper(), islower(), isdigit()