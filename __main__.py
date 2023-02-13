from Frame import *
import time
#Cria objetos
frame = Frame()

#TODO classe de controle (do programa, não do personagem. Score, status, etc...)
status = True
game_start = time.time()
game_time = 0
count = 0
lista_de_intervalos = []

while status:

    #TODO se tecla for pressionada chama o mover personagem
    #TODO movimentações dos inimigos

    #TODO classe de colisoes - verificações para sair do loop (se ... , status = False)

    frame.drawFrame()
    if WConio2.kbhit():
        frame.input(WConio2.getkey())
    
    game_time = time.time() - game_start
    #print(game_time)
    #7.3180103302001955555
    #print(count)

    if game_time >= 1:

        if count % frame.enemy1.speed == 0:
            print("gtime: ", round(game_time,2))
            frame.enemy1Move()
            print(count)
        #TODO if de acordo com a velocidade do vilao (quanto maior velocidade, mais vezes deve entrar no IF) que executa o frame.enemy1.move
    count += 1

#fora do While: game over
#TODO game over