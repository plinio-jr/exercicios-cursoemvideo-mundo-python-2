#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
opcao = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while opcao in 'Ss':
    num = int(input("Digite um numero: "))
    soma += num
    cont += 1
    if cont ==1:
      maior = menor = num
    else:
      if num > maior:
        maior = num
      else:
        num < menor
        menor = num
    opcao = str(input("Quer continuar: [S/N]")).upper().strip()[0]
media = soma / cont
print(f"Voce digitou {cont} numeros e a media foi de {media}, o menor numero foi {menor} e o maior foi {maior}")
print("Acabou")
