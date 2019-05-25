#-*- coding: utf-8 -*-

saldo = input("Informe seu saldo bancario: ")

correcao = input("Infomre a taxa de correcao: ")

anos = input("Informe a quantidade de anos que o dinheiro ficara aplicado: ")

saldo = float(saldo)

correcao = float(correcao)

anos = int(anos)

saldo_final = saldo * (1 + correcao/100) ** anos

print("Seu saldo de " + str(saldo) + " ao final de " + str(anos) + " ano(s) irá render " + str(round(saldo_final,2)))