#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um numero para ver a sua tabuada: "))
for multiplicador in range(1,11):
  print(f"{numero} X {multiplicador} = {numero * multiplicador}")
