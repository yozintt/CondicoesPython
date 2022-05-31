I = int(input('Qual a idade do nadador? '))
if I >= 5 and I <= 7:
    print('Infantil A')
elif I >= 8 and I <= 10:
    print('Infantil B')
elif I >= 11 and I <= 13:
    print('Juvenil A')
elif I >= 14 and I <= 17:
    print('Juvenil B')
else:
    print('Sênior')