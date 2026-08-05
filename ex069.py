#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
total18 = 0
totalhomem = 0
totalmulher20 = 0
while True:
  print('-'*20)
  print("CADASTRE UMA PESSOA")
  print('-'*20)
  idade = int(input("Idade: "))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    opcao =' '
    if idade >= 18:
      total18 += 1
    if sexo =='M':
      totalhomem += 1
    if idade <20 and sexo =='F':
      totalmulher20 += 1
  while opcao not in 'SN':
      opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if opcao =='N':
      break
print(f"O total de pessoas com mais de 18 anos são {total18}")
print(f"O total de homens cadastrados foram de {totalhomem}")
print(f"O total de mulheres com menos de 20 anos foi de {totalmulher20}")