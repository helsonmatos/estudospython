num = input('Digite um número: ')
print(f'\033[42mAnalisando seu número:\033[m {num}')
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')