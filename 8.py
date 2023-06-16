from itertools import product

for x in product('ЛЕТО', repeat=4):
    s = ''.join(x)
    print(s)

for a in 'ЛЕТО':
    for b in 'ЛЕТО':
        for c in 'ЛЕТО':
            for d in 'ЛЕТО':
                s = a + b + c + d
                print(s)
