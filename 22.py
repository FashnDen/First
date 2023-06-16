f = open("22.txt").read().split("\n")
m = {}
for i in f:
    s = i.split()
    if s[2] == '0':
        m[s[0]] = int(s[1])
    else:
        w = s[2].split(";")
        sp = []
        for j in w:
            j = j.replace(" ", "")
            sp.append(int(m[j]))
        m[s[0]] = int(s[1]) + max(sp)
print(max(m.values()))