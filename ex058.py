#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10")
print("Sera que voce consegue advinhar qual foi?")
certo = False
contador =0
while not certo:
  jogador = int(input("Seu palpite: "))
  contador = contador + 1
  if jogador == computador:
    certo = True
    print(f'Acertou com {contador} tentativas. Parabens')
  elif jogador < computador:
    print("Mais... Tente novamente")
  elif jogador > computador:
    print("Menos... Tente novamente")
  else:
    print('Valor Invalido! Por favor tente novamente')
    jogador = int(input("Seu palpite: "))