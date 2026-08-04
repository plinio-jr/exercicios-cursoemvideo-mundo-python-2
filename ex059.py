#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: 
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
valor_1 = int(input("Primeiro valor: "))
valor_2 = int(input("Segundo valor: "))
menu = 0
while menu !=5:
  print("""
      [1] - Somar
      [2] - Multiplicar
      [3] - Maior
      [4] - Novos numeros
      [5] - Sair
      """)
  menu = int(input("Qual a sua opção? "))
  if menu == 1:
    soma = valor_1 + valor_2
    print(f"A soma dos valores {valor_1} + {valor_2} é {soma}")
  elif menu == 2:
    mult = valor_1 * valor_2
    print(f"A multiplicação dos valores {valor_1} X {valor_2} é {mult}")
  elif menu ==3:
    if valor_1 > valor_2:
      maior = valor_1
    else:
      maior = valor_2
    print(f"entre os valores {valor_1} e {valor_2}, o maior valor é {maior}")
  elif menu ==4:
    valor_1 = int(input("Digite um novo primeiro valor: "))
    valor_2 = int(input("Digite um novo segundo valor: "))
    print(f"Os novos valores são: {valor_1} e {valor_2}")
  elif menu ==5:
    print("Programa finalizando...")
  else:
    print("Opção invalida, tente novamente!")

