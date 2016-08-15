#!/usr/bin/python
# -*- coding: utf8 -*- 

import socket,os

HOST = '191.52.64.227'     
PORT = 3001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input('Deseja iniciar o jogo pressione ENTER')
print(tcp.recv(2048))
while msg <> (' Voce Ganhou' or ' Voce Perdeu'):
    msg = raw_input('Digite uma letra> ')
    tcp.send (msg)
    msg = tcp.recv(2048)
    print msg
tcp.close()
