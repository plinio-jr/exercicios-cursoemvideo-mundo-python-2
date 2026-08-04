#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
somamedia = 0
somaidade = 0
maioridade = 0
homemvelho = ''
mulhermenor = 0

# Programa principal(MAIN)

for c in range(1, 5):
    print(f'---- {c} PESSOA ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [ M/F ]: ').lower().strip()

    somaidade += idade

    if sexo == 'm' or sexo == 'f':
        if sexo == 'f':
            if idade <= 20:
                mulhermenor += mulhermenor
        else:
            if c == 1:
                maioridade = idade
                homemvelho = nome
            else:
                if idade > maioridade:
                    maioridade = idade
                    homemvelho = nome

    else:
        print('VALOR INVÁLIDO!')
        print('Considerando [ M ]...')
        sexo = 'm'

        if sexo == 'm':
            if c == 1:
                maioridade = idade
                homemvelho = nome
            else:
                if idade > maioridade:
                    maioridade = idade
                    homemvelho = nome
# PROGRAMA FINAL

somamedia = somaidade / c

print(f'O homem com a maior idade foi {homemvelho}, cuja idade é {maioridade}')
print(f'São no total {mulhermenor} de mulheres menores de 20 anos')
print(f'A média de idade foi de {somamedia}')