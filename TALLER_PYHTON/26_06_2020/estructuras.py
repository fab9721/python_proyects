lista = list(range(1,101))

for elemento in lista:
    print (elemento, end = '')
    print()

    i=0
    while i < 20:
        print('valor de i:{}'.format(i))
        i+=1

for i in range(1,100):
    if i ==10:
        break
    print(i)

for i in range (1,101):
    for j in range(i,101):
        if j % 2 == 0:
            print('{} es par'.format(j))
            break
    else:
            print('{} no es par'. format(i))    