v = int(input(''))
p = int(input(''))

arraydiv = list()

for i in range(0, p):
    arraydiv.append(int(v / p))

sdiv = sum(arraydiv)

if v % p == 0:
    for v in arraydiv:
        print(v)
else:
    i = 0
    while sdiv < v:
        arraydiv[i] += 1
        sdiv = sum(arraydiv)
        i += 1
    for v in arraydiv:
        print(v)