#-*- coding: utf-8 -*-

usuarios_correntes = ("usuario1", "usuario2", "usuario3", "usuario4", "usuario5", "usuario6")

usuarios_novos = ("UsuAriO5", "uSuaRio6", "usUARio7", "usuario8", "usuario9")

usuarios_repetidos = []

usuarios_disponiveis = []

for usuario_novo in usuarios_novos:
    if usuario_novo.lower() in usuarios_correntes:
        usuarios_repetidos.append(usuario_novo)
    else:
        usuarios_disponiveis.append(usuario_novo)

print("Usuários disponíveis: " + str(usuarios_disponiveis))

print("Usuários repetidos: " + str(usuarios_repetidos))