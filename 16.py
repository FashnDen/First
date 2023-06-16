def F(n):
    if n >= 2222:
        return n
    if n < 2222:
        return F(n + 5) + 7
print(F(45) - F(49))