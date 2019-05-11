#-*- coding: utf-8 -*-

idade = input("Informe sua idade: ")

idade = int(idade)

if idade >= 0 and idade < 2:
    print("Você é um bebe")
elif idade >= 2 and idade < 4:
    print("Você é uma criança")
elif idade >= 4 and idade < 13:
    print("Você é um(a) garoto(a)")
elif idade >= 13 and idade < 20:
    print("Você é um(a) adolescente")
elif idade >= 20 and idade < 65:
    print("Você é um adulto")
elif idade >= 65:
    print("Você é um idoso")
else:
    print("Idade invalida")