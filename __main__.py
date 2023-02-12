from Frame import *

#Cria objetos
frame = Frame()

#TODO classe de controle (do programa, não do personagem. Score, status, etc...)
count = 0 
status = True

while status:

    #TODO classe de colisoes - verificações para sair do loop (se ... , status = False)

    frame.drawFrame()
    if WConio2.kbhit():
        frame.input(WConio2.getkey())

    count += 1 #ao final do While

#fora do While: game over
#TODO game over