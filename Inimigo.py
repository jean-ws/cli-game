from Personagem import Personagem

class Inimigo(Personagem):
    #atributos que TODOS inimigos terão
    pass

class InimigoNormal(Inimigo):
    #atributos que somente o inimigo normal terá

    def __init__(self, icon, posicao, tamanho, velocidade):
        self.icon = icon #lista[linha de cima, linha de baixo]
        self.posicao = posicao #lista[x,y]
        self.tamanho = tamanho #lista[n,n] onde o tamanho é NxN
        self.velocidade = velocidade 

        self.hitbox = [
            [self.posicao], #char principal
            [self.posicao[0] + 1, self.posicao[1]], 
            [self.posicao[0], self.posicao[1] + 1], 
            [self.posicao[0] + 1,self.posicao[1] + 1]
            ]
    
    def _alteraHitbox(self):
        self.hitbox = [
            [self.posicao], #char principal
            [self.posicao[0] + 1, self.posicao[1]], 
            [self.posicao[0], self.posicao[1] + 1], 
            [self.posicao[0] + 1,self.posicao[1] + 1]
            ]

    #TODO movimentação. Altera a posição
