#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: – EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
print("ANALISADOR DE TRIANGULOS")
area_1 = float(input("Primeiro segmento: "))
area_2 = float(input("Segundo segmento: "))
area_3 = float(input("Terceiro segmento: "))
if area_1 < area_2 + area_3 and area_2 <area_1 + area_3 and area_3 <area_2 + area_1:
  print("Os segmentos acima podem formar o triangulo")
  if area_1 == area_2 == area_3:
    print("equilatero")
  elif area_1 != area_2 != area_3 != area_1:
    print("escaleno")
  else:
    print("isosceles")
else:
  print("Os segmentos acima não podem formar um triangulo")