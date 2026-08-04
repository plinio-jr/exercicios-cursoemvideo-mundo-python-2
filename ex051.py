#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('='*40)
print('10 TERMOS DE UMA PA')
print('='*40)
termo= int(input("Digite um termo: "))
razao = int(input("Digite uma razão: "))
calculo = termo+ (10-1) * razao
for resultado in range(termo,calculo+razao,razao):
  print(resultado)
print("ACABOU!")
