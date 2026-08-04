#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('='*40)
print('10 TERMOS DE UMA PA')
num = int(input("Digite um termo: "))
razao = int(input("Digite a razão: "))
termo = num
contador = 1
while contador<= 10:
  print(f"{termo}")
  termo = termo + razao
  contador = contador + 1
print("Acabou!")