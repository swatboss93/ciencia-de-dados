#-*- coding: utf-8 -*-

acoes = {'GM': 'General Motors','CAT': 'Caterpillar', 'EK': 'Eastman Kodak'}

compras = [('GM', 100, '10/09/2001', 48), ('CAT', 100, '01/04/1999', 24), ('GM', 200, '01/06/1998', 56)]

total_arrecadado = {}

for simbolo in acoes.keys():
    total_arrecadado[simbolo] = 0

print("Relatório geral:\n")
for compra in compras:
    simbolo = compra[0]
    total_arrecadado[simbolo] += compra[1] * compra[3]
    total_compra = compra[1] * compra[3]
    print(simbolo, acoes[simbolo], compra[1], compra[2], compra[3], total_compra)

print("\n-----------------------------------------------------------------\n")

print("Resumo de compras:\n")
for simbolo, empresa in acoes.items():
    print(simbolo, empresa, total_arrecadado[simbolo])