#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input("Digite um numero para calcular seu fatorial: "))
fatorial = num
contador = 1
while fatorial > 0:
  print(f'{fatorial}')
  print('x' if fatorial > 1 else '=')
  contador *= fatorial
  fatorial = fatorial - 1
  print(f"O fatorial de {num} é {fatorial}")
