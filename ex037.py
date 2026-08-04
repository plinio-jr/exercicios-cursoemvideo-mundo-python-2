#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um numero inteiro: "))
print("Escolha uma dessas bases para a conversão:")
print("[1] - Converter para BINARIO")
print("[2] - Converter para OCTAL")
print("[3] - Converter para HEXADECIMAL")
opcao = int(input("Sua opçaõ:"))
if opcao ==1:
  binario = bin(num)[2:]
  print(f"{num} convertido para BINARIO é igual a {binario}")
elif opcao ==2:
  octal = oct(num)[2:]
  print(f"{num} convertido para OCTAL é igual a {octal}")
elif opcao ==3:
  hexadecimal = hex(num)[2:]
  print(f"{num} convertido para HEXADECIMAL é igual a {hexadecimal}")
else:
  print("Opção invalida, tente novamente!")