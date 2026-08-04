#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
num_a = int(input("Primeiro valor: "))
num_b = int(input("Segundo valor: "))
if num_a > num_b:
  print(f"O PRIMEIRO Valor {num_a} é maior")
elif num_b > num_a:
  print(f"O SEGUNDO Valor {num_b} é maior")
else:
  ("Os valores são Iguais")