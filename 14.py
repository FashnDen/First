# x = 7**103 + 20 * 7**204 - 3 * 7**57 + 97
# a = []
# while x > 0:
#     a = [x%7] + a
#     x = x // 7
# print(a.count(6))

# x = 7**103 + 6 * 7**104 - 3 * 7**57 + 98
# a = []
# while x > 0:
#     a += [x%7]
#     x //= 7
# print(sum(a))

# x = 6**203 + 5 * 6**405 - 3 * 6**144 + 76
# a = []
# while x > 0:
#     a += [x%6]
#     x //= 6
# print(a.count(0) - a.count(5))

# x = 17**5 + 85**8 - 10
# a = []
# while x > 0:
#     a += [x%17]
#     x //= 17
# print(a.count(16))

# x = 7**2 + 49**4 - 21
# a = []
# while x > 0:
#     a += [x%14]
#     x //= 14
# print(a.count(10) + a.count(0))

# Параметр
# for x in range(1,100):
#     t = 81**20 - 9**x + 50
#     a = []
#     while t>0:
#         a += [t%9]
#         t //= 9
#     if sum(a)==138:
#         print(x)

# for x in range(1,200):
#     t = 64**12 - 8**14 + x
#     a = []
#     while t>0:
#         a += [t%8]
#         t //= 8
#     if a.count(7)==12 and a.count(1)==1:
#         print(x)
# for x in range(1,200):
#     t = oct(64**12 - 8**14 + x)[2:]
#     if t.count('7') == 12 and t.count('1') == 1:
#         print(x)

# # переменная в числе
# for x in '0123456789abcdefgh':
#     a = int(f'9009{x}', 18) + int(f'2257{x}', 18)
#     if a % 15 == 0:
#         print(x, a//15)
#
# # разложение(сначала раскладываем по разрядам)
# for x in range(18):
#     a = 11*18**4 + 2*18**3 + 5*18**2 + 16*18 + 2*x
#     if a%15==0:
#         print(x, a//15)

# # Два параметра(ответ: частное)
# for x in '123456789abcdefghijkl':
#     for y in '0123456789abc':
#         a = int(f'{x}23{x}5', 22) - int(f'67{y}9{y}', 13)
#         if a%57==0:
#             print(x, y, int(x,22) + int(y,13), a//57)

# # Уравнение c неизвестной СС(Разложение или Int(Геморой))
# for n in range(2, 40):
#     if n**2 + 2*n + 3 == 9*(n+2) + 3:
#         print(n)
#
# for n in range(2,40):
#     try:
#         if int('123',n) == int('93', n+2):
#             print(n)
#     except:
#         pass

# Исследуем
# for n in range(2,40):
#     x1 = 56
#     a1 = []
#     while x1 > 0:
#         a1 += [x1%n]
#         x1 //= n
#     x2 = 45
#     a2 = []
#     while x2 > 0:
#         a2 += [x2%n]
#         x2 //= n
#     if a1[::-1][-1] == 1 and a2[::-1][-1] == 1:
#         print(n)
#
# for n in range(2,40):
#     x1 = 56
#     x2 = 45
#     if x1 % n == 1 and x2 % n == 1:
#         print(n)

# for n in range(2,100):
#     if 338%n==2 and n**2<=338<n**3:
#         print(n)

# for n in range(2,100):
#     x = 338
#     a = []
#     while x>0:
#         a += [x%n]
#         x //= n
#     if 338%n==2 and len(a) == 3:
#         print(n)

# # Перебор чисел до
# for x in range(1,51):
#     b = bin(x)[2:]
#     if len(b) >= 3 and b[-3] + b[-2] + b[-1] == '011':
#         print(x)#В ответ кол-во чисел

# for x in range(3,51):
#     if x%3==1 and x//3%3==2:
#         print(x)

# for x in range(1,101):
#     if x%16==12:
#         print(x)

# #Длина числа в СС
# for x in range(10,100):
#     if x%16==10 and x%5==3:
#         print(x)

# for x in range(1,1000):
#     if 27<=x<81 and 49<=x<343 and x%8==7 and x//8%8==1:
#         print(x)

