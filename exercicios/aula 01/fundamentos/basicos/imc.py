#-*- coding: utf-8 -*-

altura = input("Informe sua altura em metros: ")

peso = input("Informe seu peso em kilos: ")

altura = float(altura)

peso = float(peso)

imc = peso/altura**2

if imc < 18.5:
    print("Seu imc é de: " + str(round(imc,1)) + " e está abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("Seu imc é de: " + str(round(imc,1)) + " e está com peso normal")
elif imc >= 25 and imc < 29.9:
    print("Seu imc é de: " + str(round(imc,1)) + " e está com sobrepeso")
elif imc >= 30 and imc < 34.9:
    print("Seu imc é de: " + str(round(imc,1)) + " e está com obesidade grau 1")
elif imc >= 35 and imc < 39.9:
    print("Seu imc é de: " + str(round(imc,1)) + " e está com obesidade grau 2")
elif imc >= 40:
    print("Seu imc é de: " + str(round(imc,1)) + " e está com obesidade grau 3")