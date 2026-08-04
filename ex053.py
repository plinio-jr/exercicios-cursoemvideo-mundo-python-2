#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
frase = str(input("Digite uma frase: ")).strip().upper()
polindromo = frase.split()
juntar = ''.join(polindromo)
espaco = ''
for valores in range(len(juntar)-1,-1,-1):
  espaco+= juntar[valores]
print(juntar,espaco)
if espaco ==juntar:
  print("Temos um polidromo!")
else:
  print("Não é um polidromo")