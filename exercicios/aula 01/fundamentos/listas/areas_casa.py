#-*- coding: utf-8 -*-

patio = 11.25
cozinha = 18.0
sala = 20.0
quarto = 10.75
banheiro = 9.50

areas = [patio, cozinha, sala, quarto, banheiro]

print("Áreas: " + str(areas))

areas_e_comodos = ["patio", patio, 
                   "cozinha", cozinha, 
                   "sala", sala, 
                   "quarto", quarto, 
                   "banheiro", banheiro]

print("Áreas e comdoos: " + str(areas_e_comodos))

print("Segunda área: " + str(areas[1]))

print("Área sala: " + str(areas[3]))

print("Última área: " + str(areas[-1]))

print("Soma da cozinha e quarto: " + str(areas[1] + areas[3]))

print("Área do banheiro antes de mudar: " + str(areas[-1]))

areas[-1] = 10.5

print("Área do banheiro depois de mudar: " + str(areas[-1]))

print("Sala antes de mudar: " + str(areas_e_comodos[4]))

areas_e_comodos[4] = "sala de jantar"

print("Sala depois de mudar: " + str(areas_e_comodos[4]))

print("Lista antes de adicionar piscina e garagem: " + str(areas))

areas.insert(0, 24.5)

areas.append(15.45)

print("Lista depois de adicionar piscina e garagem: " + str(areas))

print("Remove nome e área do quarto - Antes: " + str(areas_e_comodos))

del(areas_e_comodos[6])
del(areas_e_comodos[6])

print("Remove nome e área do quarto - Depois: " + str(areas_e_comodos))

comodos = ["piscina", "patio", "cozinha", "sala", "quarto", "banheiro", "garagem"]

print("Áreas ordenadas" + str(sorted(areas)))

print("Comodos ordenados: " + str(sorted(comodos)))