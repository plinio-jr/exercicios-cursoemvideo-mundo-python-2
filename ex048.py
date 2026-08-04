#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for num in range(1,501,2):
  if num % 3 ==0:
    cont = cont + 1
    soma = soma + num
print(f"A soma de todos os valores foram {soma}, a quantidade de numeros é {cont}")