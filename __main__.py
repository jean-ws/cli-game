from aldair import Heroi
import Inimigo
import Tela

#Cria objetos
tela = Tela()
hero = Heroi(['ÕÕ', 'µ '],[30,16],[2,2],3)
i1, i2, i3, i4 = Inimigo() #só para existirem objetos instanciados por enquanto

#TODO classe de controle (do programa, não do personagem. Score, status, etc...)
cont = 0 
status = True

while status:
    tela.desenhaTela(hero,i1, i2, i3, i4)

    #TODO movimentações
    #TODO verificações para sair do loop (se ... , status = False)

    cont += 1 #ao final do While


#fora do While: game over
