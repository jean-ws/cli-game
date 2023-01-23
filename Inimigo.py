from Personagem import Personagem

#TODO classe de todos inimigos
class Inimigo(Personagem):
    #atributos que TODOS inimigos terão
    pass

class InimigoNormal(Inimigo):
    #atributos que somente o inimigo normal terá

    def __init__(self):
        self.icon = ["@@","@@"] #lista[linha de cima, linha de baixo]
        self.posicao = [38,16] #lista[x,y]
        self.velocidade = 3 

        self.hitbox = [
            [self.posicao], #char principal
            [self.posicao[0] + 1, self.posicao[1]], 
            [self.posicao[0], self.posicao[1] + 1], 
            [self.posicao[0] + 1,self.posicao[1] + 1]
            ]
    
    def _attHitbox(self):
        self.hitbox = [
            [self.posicao], #char principal
            [self.posicao[0] + 1, self.posicao[1]],
            [self.posicao[0], self.posicao[1] + 1], 
            [self.posicao[0] + 1,self.posicao[1] + 1] 
            ]

    #TODO movimentação. Altera a posição
