#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input("Qual o seu peso? (Kg)"))
altura = float(input("Qual a sua altura? (m)"))
imc = peso / (altura**2)
print(f"O seu IMC é {imc:.1f}")
if imc <18.5:
  print(f"Você esta abaixo do peso ideal")
elif 18.5 <=25:
  print(f"Você está no peso ideal")
elif 25 <=imc <=30:
  print(f"Você esta sobrepeso ideal")
elif imc <=40:
  print(f"Você está em obesidade")
else:
  print(f"Você esta em obesidade morbida, CUIDADO!")