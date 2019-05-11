#-*- coding: utf-8 -*-

patio = 11.25
cozinha = 18.0
sala = 20.0
quarto = 10.75
banheiro = 9.50

areas = [patio, cozinha, sala, quarto, banheiro]

for area in areas:
    print("Área: " + str(area))

areas_e_comodos = ["patio", patio, 
                   "cozinha", cozinha, 
                   "sala", sala, 
                   "quarto", quarto, 
                   "banheiro", banheiro]

for i in range(0,10,2):
    print("Comodo: " + str(areas_e_comodos[i]) + "\nÁrea: " + str(areas_e_comodos[i+1]) + "\n")

print("Maior área: " + str(max(areas)))

print("Menor área: " + str(min(areas)))

media = sum(areas)/len(areas)

print("Média área: " + str(media))

andares_de_baixo = areas_e_comodos[0:6]

print("Comodos de baixo: " + str(andares_de_baixo))

andares_de_cima = areas_e_comodos[6:9]

print("Comodos de cima: " + str(andares_de_cima))

andares_de_baixo = areas_e_comodos[:6]

print("Comodos de baixo sem indice inicial: " + str(andares_de_baixo))

andares_de_cima = areas_e_comodos[6:]

print("Comodos de cima: " + str(andares_de_cima))