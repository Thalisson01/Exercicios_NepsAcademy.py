matriz = list()

dados = list(map(int, input('').split()))

for i in range(dados[0]):
    matriz.append(list(map(int, input('').split())))

print('aaaaaaaaaaaaaaa')

for i in range(dados[0]):
    for j in matriz[i]:
        print(j, end=' ')
    print('')

direito = 0

M = True

n = 0
po = 2

for i in range(dados[0]):
    for j in range(len(matriz[i])):
        if (i == 0):
            if (j == 0):
                if (matriz[i][j] == 1):
                    matriz[i][j] = po
            else:
                if (matriz[i][j] == 1):
                    while True:
                        n += 1
                        for k in range(j, len(matriz[i])-1):
                            if (matriz[i][j+1] == 1):
                                matriz[i][j] = 2
                        break


        


            

print('aaaaaaaaaaaaaaa')

for i in range(dados[0]):
    for j in matriz[i]:
        print(j, end=' ')
    print('')