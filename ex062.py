#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('='*40)
print('10 TERMOS DE UMA PA')
num = int(input("Digite um termo: "))
razao = int(input("Digite a razão: "))
termo = num
contador = 1
total = 0
novo= 10
while novo !=0:
  total = total + novo
  while contador<= total:
    print(f"{termo}")
    termo = termo + razao
    contador = contador + 1
  print("Pausa")
  novo = int(input("Quantos termos voce quer mostrar a mais: "))
print("Acabou!")