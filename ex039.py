#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input("Ano de nascimento: "))
idade = atual - ano
alistamento = ano + 18
diferenca = 18 - idade
atraso = idade - 18
print(f"Quem nasceu em {ano} tem {idade} anos em 2026.")
if idade < 18:
  print(f"Ainda faltam {diferenca} para voce se alistar. Seu alistamento sera no ano de {alistamento}")
elif idade ==18:
  print(f"Voce tem {idade}, esse ano: {ano} voce precisa se alistar IMEDIATAMENTE.")
else:
  print(f"Voce tem {idade} anos, Seu alistamento foi em {alistamento}, Voce deveria ter se alistado a {atraso} anos")