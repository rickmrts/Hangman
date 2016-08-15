#!/usr/bin/python
# -*- coding: utf8 -*- 

import socket,os

SIZE = 2048

hangman = [
"""
            -----
            |   |
                |
                |
                |
                |
            ---------
""",
"""
            -----
            |   |
            O   |
                |
                |
                |
            ---------
""",

"""
            -----
            |   |
            O   |
            |   |
                |
                |
            ---------
""",
"""
            -----
            |   |
            O   |
            |\  |
                |
                |
            ---------
""",
"""
            -----
            |   |
            O   |
           /|\  |
                |
                |
            ---------
""",
"""
            -----
            |   |
            O   |
           /|\  |
             \  |
                |
            ---------
""",
"""
            -----
            |   |
            O   |
           /|\  |
           / \  |
                |
            ---------
"""]

HOST = ''              
PORT = 3001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
erros = 0
letraserradas = []
string_oculta = ''
palavra = raw_input('Digite a palavra> ')
string_oculta = ' _ ' * len(palavra)
while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente
    con.sendall('Comece')
    while True:
        if (string_oculta == palavra):
            print ' Voce ganhou'
            con.sendall(' Voce Ganhou')
            break
        elif erros > 5:
            print 'Voce perdeu'
            con.sendall(' Voce Perdeu')
            break
        msg = con.recv(SIZE)
        print msg
        if not msg: break
        os.system("clear")
       	if msg not in palavra:
                con.sendall('Letra errada')
       	        erros+=1
                letraserradas.append(msg)
        else:
            con.sendall('Letra correta')
            string_oculta = ''.join([msg if msg == letter else string_oculta[pos]
                   for pos, letter in enumerate(palavra)])
        print hangman[erros]
        print string_oculta
        print '\n'
        print 'Letras erradas ja tentadas: '
        print letraserradas
    print 'Finalizando conexao do cliente', cliente
    break
    con.close()