aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('=-'*20)

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 >= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('=-'*45)

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
