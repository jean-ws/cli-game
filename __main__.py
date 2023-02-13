from Frame import *
from GameOver import GameOver
from Status import *
from Score import *
from Menu import *
import time

width = 95
height = 40
score = Score()

def drawMainMenu():   
    menu = Menu(width,height)
    menu.drawScreen()
    play = False
    while not play:
        if WConio2.kbhit():
            if ' ' == WConio2.getkey():
                play = True
            #TODO elif 'r': draw scoreboard screen
            #TODO scoreboard class screen

def drawGame():
    
    frame = Frame(width,height)
    game_status = Status()
    game_start = time.time()
    game_time = 0
    count = 0

    while game_status.ingame:
        play = False

        frame.drawFrame()
        if WConio2.kbhit():
            frame.input(WConio2.getkey())
        
        game_time = time.time() - game_start

        if game_time >= 1: #waits 1 second before the enemy start to track the hero

            if count % frame.enemy1.speed == 0:
                frame.enemy1Move()

            if game_time > 10:
                frame.createEnemy2()

        game_status.verifyCollisions(frame.hero,frame.enemy1)

        score.currentScore = int(round(game_time,2)*100)

        count += 1

def drawGameOver():
    play = False

    score.verifyRecords()

    game_over = GameOver(width,height)
    game_over.drawScreen(score)
    while not play:
        if WConio2.kbhit():
            if ' ' == WConio2.getkey():
                play = True

while True:
    drawMainMenu()
    drawGame()
    drawGameOver()