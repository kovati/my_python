import operator

a_number = 31
b_number = 2
print(a_number + b_number)
print(b_number * b_number)
print(a_number ** b_number)
print(a_number ** 1)
print(a_number ** 0)
print(a_number / b_number)  # valos osztas
print(a_number // b_number)  # egesz osztas
print(2 // 3)  # egesz osztas
print(0 % 3)
print(1 % 3)
print(2 % 3)
print(3 % 3)
print(4 % 3)
print(4 % -3)
print(-4 % 3)
print(-1 % 3)
print(0 % -3)
a_number = a_number + 456  # a_number = 31 + 456 -> a_number = 487 -> a_number <- 487
print(a_number)
print(3 + 2 * 4)
print((3 + 2) * 4)
print(operator.add(3, 4))
a_number = b_number = b_number - 2
a_number *= 2  # a_number = a_number * 2
a_number = 2
a_number *= 3 + 2  # a_number *= 5 -> a_number = 2 * 5 -> a_number <- 10 ne feledd ez ertekado utasita es ennek megfeleloen alakul a precedencia is
a_number = a_number + 1
a_number += 1  # a_number++ ez nincs

print(3 < 8)
print(3 != 8)
print(3 != 3)
print(3 == 3)
print(3 < 5)  # szigoru feltetel
print(3 <= 4)  # megengedi feltetel
# igy kell csunyan programozni
print(5 * (4 < 5))  # 5 * True -> 5 * 1 -> 5
print(5 * (6 < 5))  # 5 * False -> 5 * 0 -> 0
print(bool(0))
print(bool(-5852))

print(2 == 2 and 2 == 3)  # logikai osszehasonlito operator
print(2 == 2 or 2 == 3)
print((2 == 2) ^ (2 == 3))  # bitenkenti logikai operator
print(2 ^ 2)
print(chr(ord("0") ^ 1))  # chr(48 ^ 1) -> chr(110000 ^ 000001) -> chr(110001) -> chr(49) -> '1'
print(ord("0"))
print(bin(48))
print(0 ^ 1)
print(48 ^ 1)
print(chr(ord("1") ^ 1))
print(bin(49))
print(bin(1))
print(-31 ^ 1)
print(31 ^ (-1))  # 11111111
print(bin(-1))
number = 23
print(id(23))
print(id(number))
number += 1
print(id(number))
number -= 1
print(id(number))
print(id("alma"))
a = 23
b = 23
print(a is b)
a += 1
print(a is b)
print(isinstance(a, float))  # tipus vizsgalat ("talan ebben a nyelvben nincs nagy szerepe")
print(isinstance("alma", str))
numbers = [67, 89, 45, -1, 0]
print(0 in numbers)
print(10 in numbers)
print("a" in "alma")
print("a" in "ALMA")
# print(0 in 1000) # error mert nem iterable
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5678 & 31)  # (31)10 -> (11111)2
print(bin(5678))  # 1011000101110 & 00000000011111 -> 0000000001110
print(~1)  # 00000001 -> 11111110
print(~(-1))  # 11111111 -> 00000000
print((~(-1)) + 1)  # 11111111 -> 00000000
pos_number = 34
pos_number = -pos_number
print(pos_number)
print(5 << 1)
print(2 << 10)  # 2 ** 10
print(20 >> 1)  # 20 // 2
print(-1 >> 23)
print(0 << 42)

#      O
#     OOO
#    OOOOO
#   OOOOOOO




