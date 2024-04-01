#Faça um programa ue leia a altura e a largura de uma parede em metros.
#Calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro
#de tinta, pinta uma área de 2 m**2


altura = float(input('Qual é a altura da parece? '))
largura = float(input('Qual é a Largura da Parede? '))
área = largura * altura
tinta = área / 2

print('Sua parede tem a dimensão {} x {} e sua área é de {}m². '.format(altura, largura, área))
print('Para pintar esse parede, você precisa de {} litros de tinta. '.format(tinta))
