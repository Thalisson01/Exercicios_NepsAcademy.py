arrayinfos = tuple(map(int, input('').split()))
array = tuple(map(int, input('').split()))
arraylist = list(array[:])

par = 0

for i in range(arrayinfos[0]):
    for k in range(i, arrayinfos[0]-1):
        soma = arraylist[i] + arraylist[k+1]
        if soma >= arrayinfos[1] and soma <= arrayinfos[2]:
            par += 1
            #print(arraylist[i], ' + ', arraylist[k+1])

print(par)