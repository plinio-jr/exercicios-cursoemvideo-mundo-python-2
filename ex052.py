#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
contador = 0
num = int(input("Digite um numero: "))
divisivel = 0
for valor in range(1, num +1):
  if num % valor==0:
    print("\033[34m")
    divisivel +=1
  else:
    print("\33[31m")
  print(valor)
print(f"O numero total foi divisivel {divisivel} vezes.")
if divisivel== 2:
  print("Por isso ele é primo!")
else:
  print("Por isso ele não é primo!")