nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print(f'\033[32mTirando {nota1} e {nota2}, a média do aluno é {media}\033[m')

if media < 5.0:
    print('O aluno está REPROVADO.')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está em RECUPERAÇÂO.') 
else:
    print('O aluno está APROVADO')