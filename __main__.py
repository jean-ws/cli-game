from Tela import *

#Cria objetos
tela = Tela()
#i1, i2, i3, i4 = Inimigo() #só para existirem objetos instanciados por enquanto

#TODO classe de controle (do programa, não do personagem. Score, status, etc...)
cont = 0 
status = True

while status:

    #TODO se tecla for pressionada chama o mover personagem
    #TODO movimentações dos inimigos

    #TODO classe de colisoes - verificações para sair do loop (se ... , status = False)

    tela.desenhaTela()
    
    cont += 1 #ao final do While

#fora do While: game over
#TODO game over