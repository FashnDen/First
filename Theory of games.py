# 1 куча
# def f(a):
#     if a >= 25:
#         return 0
#     t = [f(a + 2), f(a * 2)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n)+1
#     else:
#         return -max(t)
#
# for s in range(1, 25):
#     if f(s) == 3:
#         print(s)
# 2 кучи
# from functools import lru_cache
# @lru_cache(None)
# def f(a, b):
#     if a + b >= 68:
#         return 0
#     t = [f(a + 2, b), f(a * 3, b), f(a, b + 2), f(a, b * 3)]
#     n = [i for i in t if i <= 0]
#     if n:
#         return -max(n)+1
#     else:
#         return -max(t)
#
# for s in range(1, 60):
#     if f(8, s) == 3:
#         print(s)
# Кабанов
def f(s,m):
    if s>=34: return m%2==0
    if m == 0: return 0
    h = [f(s+1,m-1),f(s+2,m-1),f(s+3,m-1),f(s*2,m-1)]
    return any(h) if m%2!=0 else all(h)
print([s for s in range(1,34) if f(s,2)])
print([s for s in range(1,34) if not f(s,1) and f(s,3)])
print([s for s in range(1,34) if not f(s,2) and f(s,4)])