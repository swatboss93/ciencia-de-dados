#-*- coding: utf-8 -*-

nome = input("Informe seu nome com espacos antes e depois: ")

print("Nome com espacos: " + nome + "!")

print("Nome sem espacos nada direita: " + nome.rstrip() + "!")

print("Nome sem espacos nada esquerda: " + nome.lstrip() + "!")

print("Nome sem espacos nada direita e esquerda: " + nome.strip() + "!")

print("Nome minusculo: " + nome.strip().lower() + "!")

print("Nome maiusculo: " + nome.strip().upper() + "!")

print("Nome title: " + nome.strip().title() + "!")