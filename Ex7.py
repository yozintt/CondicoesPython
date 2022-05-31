N1 = float(input('Digite a sua primeira nota: '))
N2 = float(input('Digite a sua ultima nota: '))
AM = int(input('Quantas aulas ministradas na disciplina de Calculo? '))
AS = int(input('Quantas aulas assistidas na disciplina de Calculo? '))
MF = ((N1 + N2)/2)
FQ = (100 * AS ) / AM
print('A sua média final é: {:.1f}'.format(MF))
if MF >= 70:
    print('Você está aprovado!')
    if FQ >= 75:
        print('Você possui 75% ou mais de presença!')
if FQ < 75:
    print('Você reprovou por frequência...')
else: 
    print('Reprovou por média...')
