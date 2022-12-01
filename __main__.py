import os
import WConio2 #pip install WConio2 
import cursor #pip install cursor

from aldair import Heroi
import Inimigo
import Tela

#TODO prepara tela (mover para outro arquivo depois)
WConio2.clrscr()
cursor.hide() 
WConio2.textbackground(15)
WConio2.textcolor(0)

#Cria objetos
hero = Heroi(['ÕÕ', 'µ '],[30,16],[2,2],3)
i1, i2, i3, i4 = Inimigo() #só para existirem objetos instnciados por enquanto
cont = 0 #criar classe depois
status = True
tela = Tela()

while status:
    tela.desenhaTela(hero,i1, i2, i3, i4)

    #TODO verificações para sair do loop (se ... , status = False)
    cont += 1 #ao final do While


#fora do While: game over