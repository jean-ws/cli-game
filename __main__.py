import os
import WConio2 #pip install WConio2 
import cursor #pip install cursor
import time

from aldair import Heroi
from Inimigo import inimigos

#TODO prepara tela (mover para outro arquivo depois)
WConio2.clrscr()
cursor.hide() 
WConio2.textbackground(15)
WConio2.textcolor(0)

#normal = inimigos('Junin', '††__', '%20', 0, 40)
#corredor = inimigos('Capetinha', '¬¬', '%30', 15, 0)
#grande = inimigos('Big Joe', 'OOO\nOOO\nOOO', '%10', 15, 40)
#longo = inimigos('Crobinha', '¢¢¢¢¢¢¢Œ', '%15', 0, 0)

hero = Heroi(['ÕÕ', 'µ '],[30,16],[2,2],3)
cont=0

while True:
    WConio2.gotoxy(0,0)
    time.sleep(0.01)

#TODO verificações para sair do loop (se ... , status = False)

    cont += 1 #ao final do While


#fora do While: game over