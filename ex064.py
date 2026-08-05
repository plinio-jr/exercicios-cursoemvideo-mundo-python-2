#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = 0
cont= 0
soma = 0
num = int(input("Digite um numero [999 para parar]: "))
while num != 999:
    #cont = cont + 1
    cont += 1
    #soma = soma + num
    soma += num
    num = int(input("Digite um numero [999 para parar]: "))
print(f"Voce digitou {cont} numeros e a soma entre eles foi {soma}")