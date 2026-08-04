#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input("Valor da casa: R$"))
salario = float(input("Digite o valor do salario: R$"))
ano = int(input("Quantos anos de financiamento: "))
tempo = ano * 12
prestacao = casa / tempo
valor = salario * 0.3
if prestacao <= valor:
  print(f"Para pagar uma casa de {casa:.2f} em {ano} anos a prestação sera de {prestacao:.2f}. Emprestimo concedido!")
else:
  print(f"Para pagar uma casa de {casa:.2f} em {ano} anos a prestação sera de {prestacao:.2f}. Emprestimo negado!")