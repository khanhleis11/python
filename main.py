# chú thích một dòng 

"""
chú thích nhiều dòng
"""

# biến và kiểu dữ liệu
# a = 100
# b = "28tech"
# print(type(a)) # in ra kieu du lieu cua a
# print(type(b))
# print(a, b)

# biến trong py có phân biệt hoa thường
# a = 100
# b = 100.0
# c = 5 + 3j
# print(type(a), type(b), type(c), sep = "\n")

# trong py có thể xử lý số nguyên lớn dưới kiểu int
# a = 0b1001;
# print(a)

# # lam tron trong py
# a = 28.42584
# print("%.2f" % a)
# print("{:.4f}".format(a))

# # str
# s = "28tech"
# # khai bao tren nhieu dong
# s1 = """le
# quoc 
# khanh"""
# print(s, s1, sep='\n')

# a = 20.432941
# s = int(a)
# print(s, type(s))

#toán tử gán
# a, b, c = 100, 200, 300 # gán trên cùng một dòng
# print(a, b, c)

# hoán vị trong python
# a = 200
# b = 300
# a, b = b, a #hoán vị trong py
# print(a, b)

"""
Toán tử toán học
/: chia thap phan
//: chia phan nguyen
%: chia phan du
** luy thua (2**10) = 1024
"""
# print(2**10)

# Toán tử so sánh (giống C++, Java)

"""
Toán tử thành viên
"""
# s = "Le Quoc Khanh"
# name = "Khanh "
# print(name not in s) # kiểm tra xem name có trong s không?

# input(prompt: ...). Lưu ý phải ép kiểu vì mặc định là str
# a = int(input())
# print(a)

# print("Hello " + input() + "!")

# Bước 1: Nhập chuỗi
# s = input("Nhap 3 so: ")
# # Bước 2: split() chuỗi đó ra
# tmp = s.split();
# # Bước 3: chuyển hết về dạng số nguyên
# x, y, z = map(int, tmp)
# print(x + y + z)

# x, y, z = map(int, input().split())
# print(x + y + z)


# import math
# print(help(math))
# sqrt
# isqrt (Tính căn bậc hai(phần nguyên))
# ceil
# floor
# round(làm tròn theo quy tắc toán học)
# factorial
# gcd(a, b)
# comb(n, k): tổ hợp chập k của n
# max
# min
# abs
# sum
# print(math.sqrt(31))

# if 100 > 50:
#     print("I love you")
#     print("Le Quoc Khanh")


# n = int(input())
# if n % 2 == 0:
#     print("CHAN")
# else:
#     print("LE")

# elif

#for
a = range(1, 10, 1)
for i in a:
    print(i, end = " ")
print()
for i in range(1, 51):
    print(i, end = " ")
print()
for i in range(10, -1, -1):
    print(i, end=" ")

for i in range(1, 10, 0):
    print(i, end = " ")