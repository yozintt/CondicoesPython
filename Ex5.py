sexo = input('Qual o seu sexo? ex: S ou M ')

if sexo == 'H':
    h = float(input('Qual a sua altura: ex. em metros '))
    pesoIdeal = (72.7 * h) - 58
    print(pesoIdeal)
elif sexo == 'M':
    h = float(input('Qual a sua altura: ex. em metros '))
    pesoIdeal = (62.1 * h) - 44.7
    print(pesoIdeal)