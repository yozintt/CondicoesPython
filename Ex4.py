from math import sqrt
import math


A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
C = int(input('Digite o terceiro número: '))
print('{}, {}, {}'.format(A, B, C))
if A >= 0:
    print('A raiz de {} é: '.format(A), (math.sqrt(A)))
else:
    print('O quadrado de {} é '.format(A), (A**2))
if B >= 10 and B <= 100:
    print('Número está entre 10 e 100 – intervalo permitido')
    if C < B:
        print('A diferença entre {} e {} é:'.format(C, B), (B - C))
    else:
        print('{} adicionado de 1 é: '.format(C), (C + 1))