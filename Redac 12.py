a = '5' * 104
while ('555' in a) or ('11' in a) or ('2' in a):
    if '555' in a:
        a = a.replace('555', '1')
    elif '11' in a:
        a = a.replace('11', '25')
    else:
        a = a.replace('2', '5')
print(a)
