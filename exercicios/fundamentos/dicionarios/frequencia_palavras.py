#-*- coding: utf-8 -*-

palavras = ["idade", "adolescente", "festa", "brincadeira", "saude", 
            "festa", "estudo", "festa", "saude", "brincadeira", "idade",
            "festa", "festa", "festa", "saude", "brincadeira"]

frequencias = {}

for palavra in palavras:
    chave = palavra.lower()
    if chave in frequencias.keys():
        frequencias[chave] += 1
    else:
        frequencias[chave] = 1

print("A frequencia das palavras: " + str(frequencias))

palavra_mais_usada = max(frequencias.keys(), key=(lambda key: frequencias[key]))
print("A palavra mais usada foi " + str(palavra_mais_usada) + " com frequencia de " + str(frequencias[palavra_mais_usada]))

print("--------------------------------------------------------------------------------------------------------")
palavra_mais_usada = ""
maior_frequencia = 0

for palavra, frequencia in frequencias.items():
    if frequencia > maior_frequencia:
        maior_frequencia = frequencia
        palavra_mais_usada = palavra


print("A palavra mais usada foi " + str(palavra_mais_usada) + " com frequencia de " + str(maior_frequencia))