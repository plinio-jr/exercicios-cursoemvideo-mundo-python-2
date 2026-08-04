#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
nota_1 = float(input("Digite o valor da primeira nota: "))
nota_2 = float(input("Digite o valor da segunda nota: "))
media = ((nota_1 + nota_2) / 2)
if media <= 5:
  print(f"Sua media final é {media}, você está Reprovado")
elif media <7:
  print(f"Sua media final é {media}, você está de Recuperação")
else:
  print(f"Sua media final é {media}, você esta Aprovado!")