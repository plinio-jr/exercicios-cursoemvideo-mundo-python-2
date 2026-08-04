#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
jogada = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print("Suas opções:")
print("[0] - Pedra")
print("[1] - Papel")
print("[2] - Tesoura")
jogador = int(input("Qual a sua jogada:"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print('-=' *11)
print(f"O jogador jogou {jogada[jogador]}")
print(f"O computador jogou {jogada[computador]}")
print('-=' *11)
if computador ==0:
  if jogador ==0:
    print("Empate!")
  elif jogador ==1:
    print("Jogador venceu!")
  elif jogador ==2:
    print("Computador venceu!")
  else:
    print("Jogada invalida!")
if computador ==1:
  if jogador==1:
    print("Empate!")
  elif jogador == 0:
    print("Computador venceu!")
  elif jogador ==2:
    print("Jogador venceu!")
  else:
    print("Jogada invalida!")
if computador ==2:
  if jogador ==2:
    print("Empate!")
  elif jogador ==1:
    print("Computador venceu!")
  elif jogador ==0:
    print("Jogador venceu!")
  else:
    print("Jogada invalida!")