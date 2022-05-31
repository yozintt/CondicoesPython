A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
if A == B:
    print('números são iguais!')   
else:
    if A > B:
        print('{} é maior número'.format(A))
    else:
        print('{} é maior número'.format(B))