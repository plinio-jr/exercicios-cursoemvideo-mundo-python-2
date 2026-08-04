#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print("===== LOJAS ARRUDA =====")
valor = float(input("Preço das compras: "))
print("Formas de pagamento:")
print("[1] - á vista dinheiro/cheque")
print("[2] - á vista cartão")
print("[3] - 2x no cartão")
print("[4] - 3x ou mais no cartão")
opcao = int(input("Qual a sua opção: "))
if opcao ==1:
  calc = valor - (valor * 0.10)
  print(f"Sua compra de R$ {valor} vai custar R$ {calc} no final.")
elif opcao ==2:
  calc = valor - (valor * 0.05)
  print(f"Sua compra de R$ {valor} vai custar R$ {calc} no final")
elif opcao ==3:
  parcela = valor / 2
  print(f"Sua compra de R$ {valor} sera parcelada em {parcela} R$")
elif opcao ==4:
  parcela = int(input("Quantidade de parcelas"))
  calc = valor + (valor * 0.20)
  c_parcela = calc/ parcela
  print(f"Sua compra de R$ {valor} vai custar R$ {calc} no final")
  print(f"Sua compra sera parcelada em {parcela}x de {c_parcela} com juros")
else:
  print(f"Opção não encontrada. Por favor tente novamente!")