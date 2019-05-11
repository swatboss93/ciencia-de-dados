#-*- coding: utf-8 -*-

cardapio = ("macarronada", "lasanha", "pizza", "hamburguer", "risoto")

for comida in cardapio:
    print(comida)

try: 
    cardapio[-1] = "escondidinho"
except TypeError:
    print("Erro ao alterar tupla lançado com sucesso")

cardapio = ("macarronada", "lasanha", "pizza", "churrasco", "escondidinho")

for comida in cardapio:
    print(comida)