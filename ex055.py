#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista=[]
for pessoa in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(pessoa)))
    lista+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lista))  #maximo valor da lista
print('O Menor peso foi:', min(lista))  #minimo valor da lista