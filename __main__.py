from Frame import *
from GameOver import GameOver
from Status import *
import time

width = 95
height = 40
frame = Frame(width,height)
game_status = Status()

game_start = time.time()
game_time = 0
count = 0

while game_status.ingame:

    frame.drawFrame()
    if WConio2.kbhit():
        frame.input(WConio2.getkey())
    
    game_time = time.time() - game_start

    if game_time >= 1: #waits 1 second before the enemy start to track the hero

        if count % frame.enemy1.speed == 0:
            frame.enemy1Move()

    game_status.verifyCollisions(frame.hero,frame.enemy1)
    count += 1

game_over = GameOver(width,height)
game_over.drawScreen()
while True:
    pass