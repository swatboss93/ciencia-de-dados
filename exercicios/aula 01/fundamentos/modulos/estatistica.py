#-*- coding: utf-8 -*-

def calcula_media(numeros):
    quantidade = len(numeros)

    if quantidade == 0:
        return 0
    
    total = sum(numeros)

    return total / quantidade