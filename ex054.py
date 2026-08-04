#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1,8):
  nascimento = int(input(f"Em que ano a pessoa {pessoa} voce nasceu: "))
  idade = atual - nascimento
  if idade> 18:
    total_maior = total_maior+ 1
  else:
    total_menor = total_menor+ 1
print(f"temos {total_menor} pessoas que sao menores de idade")
print(f"temos {total_maior} pessoas que sao maiores de idade")