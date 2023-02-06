from Frame import *

#Cria objetos
frame = Frame()

#TODO classe de controle (do programa, não do personagem. Score, status, etc...)
count = 0 
status = True

while status:

    #TODO se tecla for pressionada chama o mover personagem
    #TODO movimentações dos inimigos

    #TODO classe de colisoes - verificações para sair do loop (se ... , status = False)

    frame.drawFrame()
    if WConio2.kbhit():
        frame.input(WConio2.getkey())
    #TODO if de acordo com a velocidade do vilao (quanto maior velocidade, mais vezes deve entrar no IF) que executa o frame.enemy1.move

    count += 1 #ao final do While

#fora do While: game over
#TODO game over