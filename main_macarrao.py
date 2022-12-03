import os
import WConio2
import cursor
import time

WConio2.clrscr()
cursor.hide()


#Aldair
heroi = '=)'
heroiX = 20
heroiY = 4

#inimigos
bicho1 = '[]'
bicho1X = 10
bicho1Y = 7

#contador de frames
cont=0

#white mode
WConio2.textbackground(15)
WConio2.textcolor(0)

#logica geral
while True:
    WConio2.gotoxy(0,0)
    time.sleep(0.01)
    #mapa
    
    tamanho_lateral_do_frame = 60
    
    print('-'* (tamanho_lateral_do_frame + 2))#teto
    for j in range(26):
        print('|', end='')#parede esquerda

        #printa menos espaços na linha com o vilao
        #if bicho1Y == j:
        #    tamanho_lateral_do_frame -= 2
        if heroiY == j:
            linha_atual = tamanho_lateral_do_frame - 2
        else:
            linha_atual = tamanho_lateral_do_frame

        for k in range(linha_atual):
            char = ' '
            
            if j==bicho1Y and k==bicho1X:
                char=bicho1
            
            if j==heroiY and k==heroiX:
                char=heroi

            print(char, end='')

        print('|')#parede direita
    print('-'*62)#chão

    #controle inimigos
    # Largura do bicho - tamanho do mapa    
    if cont%20 == 0: # % e a velocidade do inimigo
        bicho1X+=1
    if bicho1X > 58:
        bicho1X=0
    if cont%20 == 0:
        bicho1Y+=1
    if bicho1Y > 58:
        bicho1Y=0

    #pegando comandos do teclado
    if WConio2.kbhit():
        (key, symbol) = WConio2.getch()

        if symbol=='a':
            heroiX-=1
        elif symbol=='d':
            heroiX+=1
        elif symbol=="w":
            heroiY-=1
        elif symbol=="s":
            heroiY+=1
        elif symbol==' ':
            heroiY+=9
    if bicho1X == heroiX and bicho1Y == heroiY:
        break 
    cont+=1


