from Frame import *
from Status import *
import time
#Cria objetos
frame = Frame()
game_status = Status()
game_start = time.time()
game_time = 0
count = 0

while game_status.ingame:

    #TODO movimentações dos inimigos

    #TODO classe de colisoes - verificações para sair do loop (se ... , status = False)

    frame.drawFrame()
    if WConio2.kbhit():
        frame.input(WConio2.getkey())
    
    game_time = time.time() - game_start

    if game_time >= 1: #waits 1 second before the enemy start to track the hero

        if count % frame.enemy1.speed == 0:
            frame.enemy1Move()

    game_status.verifyCollisions(frame.hero,frame.enemy1)
    count += 1

