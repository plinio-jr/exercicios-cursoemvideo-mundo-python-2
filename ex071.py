#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:considere que o caixa possui cédulas de R 50,R 20, R 10eR 1.
print('='*30)
print("Banco novo")
print("="*30)
valor = int(input("Que valor você quer sacar: "))
total = valor
cedula = 50
totalcedula = 0
while True:
  if total >= cedula:
    total -= cedula
    totalcedula += 1
  else:
    if totalcedula >0:
      print(f"O total é {totalcedula} e sera entregue cedulas de R$ {cedula}")
    if cedula == 50:
      cedula = 20
    elif cedula ==20:
      cedula = 10
    elif cedula == 10:
      cedula =5
    elif cedula == 5:
      cedula =1
    totalcedula = 0
    if total ==0:
      break
print("="*30)
print("Volte sempre!!")