#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
calculo_idade = 0
media_idade = 0
max_homem = 0
total_mulher = 0
nome_velho = ''
for p in range(1,5):
  print('-----'f'pessoa {p}''-----')
  nome = str(input("Nome: "))
  idade = int(input("Idade: "))
  sexo = str(input("Sexo[M/F]: "))
  calculo_idade += idade
  media_idade =calculo_idade /4
  if sexo in"Mm" and idade:
    max_homem = idade
    nome_velho = nome
  if p ==2 and sexo in"Ff":
     if idade <= 20:
      total_mulher += total_mulher
media_idade = calculo_idade / p
print(f'A media de idade do grupo é de {media_idade}')
print(f"O homem mais velho tem {max_homem} e se chama {nome_velho}")
print(f"Ao todo são {total_mulher} mulheres com menos de 20 anos")