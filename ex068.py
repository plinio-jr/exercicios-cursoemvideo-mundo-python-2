#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:
  print("-="*15)
  print("Vamos Jogar par ou impar!")
  print("-="*15)
  jogador = int(input('Diga um valor: '))
  computador = randint(0,10)
  total = jogador + computador
  opcao = ' '
  while opcao not in 'PI':
    opcao = str(input("Par ou Impar? [P/I]: ")).strip().upper()[0]
  print(f"Você jogou {jogador} e o computador jogou {computador} . total de {total}")
  print("Deu par" if total % 2 == 0 else total % 2 ==1)
  if opcao =='P':
      if total % 2 == 0:
        print("O jogador venceu")
        vitoria += 1
      else:
        print("Voce perdeu")
        break
  elif opcao=='I':
    if total % 2 ==1:
      print("O jogador venceu")
      vitoria += 1
    else:
      print("Voce perdeu")
      break
  print("Vamos jogar novamente")
print(f"Game over! voce venceu {vitoria} vezes")