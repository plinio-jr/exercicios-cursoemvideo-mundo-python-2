#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = totalmil = menor = cont = 0
barato = ' '
while True:
  print('-'*20)
  print('Loja super baratao')
  print('-'*20)
  nome = str(input("Nome do produto: "))
  preco = float(input("Preço: R$ "))
  cont += 1
  total = preco + total
  if preco > 1000:
    totalmil +=1
  if cont ==1 or preco < menor:
      menor = preco
      barato = nome
  else:
      if preco < menor:
        menor = preco
        barato = nome
  opcao = ' '
  while opcao not in 'SN':
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if opcao =='N':
      break
print(f"O total da compra foi de {total} R$")
print(f"O temos {totalmil} produto(s) que passaram de 1000 R$")
print(f"O produto mais barato é {barato} custando {menor} R$")
print("-"*20)
print("Fim do programa")
print("-"*20)