#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:0 – 1 – 1 – 2 – 3 – 5 – 8
print('-'*30)
print("Sequencia de Fibonacci")
print('-'*30)
num = int(input("Quantos termos voce quer mostrar: "))
t1= 0
t2= 1
cont = 3
while cont <= num:
  t3 = t1 + t2
  t1 = t2
  t2 = t3
  cont = cont+ 1
  print('~'*30)
  print(f"{t1} -> {t2} -> {t3}")
  print('~'*30)
print('Fim')