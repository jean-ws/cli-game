import os
import WConio2
import cursor
import time

from aldair import Heroi
from enemy import inimigos

WConio2.clrscr()
cursor.hide()

#Cor
WConio2.textbackground(15)
WConio2.textcolor(0)

normal = inimigos('Junin', '††__', '%20', 0, 40)
corredor = inimigos('Capetinha', '¬¬', '%30', 15, 0)
grande = inimigos('Big Joe', 'OOO\nOOO\nOOO', '%10', 15, 40)
longo = inimigos('Crobinha', '¢¢¢¢¢¢¢Œ', '%15', 0, 0)

cont=0

hero = Heroi()

while True:
    WConio2.gotoxy(0,0)
    time.sleep(0.01)

    if hero.posicao_X == normal.posicao_inimigo_X and hero.posicao_Y == normal.posicao_inimigo_Y:
        break

    cont += 1



#fora do While: game over