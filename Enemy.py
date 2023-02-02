from Character import Character

#TODO classe de todos inimigos
class Enemy(Character):
    #atributos que TODOS inimigos terão
    pass

class NormalEnemy(Enemy):
    #atributos que somente o inimigo normal terá

    def __init__(self):
        self.icon = ["@@","@@"] #lista[linha de cima, linha de baixo]
        self.position = [38,16] #lista[x,y]
        self.speed = 3 

        self.hitbox = [
            [self.position], #char principal
            [self.position[0] + 1, self.position[1]], 
            [self.position[0], self.position[1] + 1], 
            [self.position[0] + 1,self.position[1] + 1]
            ]
    
    def _attHitbox(self):
        self.hitbox = [
            [self.position], #char principal
            [self.position[0] + 1, self.position[1]],
            [self.position[0], self.position[1] + 1], 
            [self.position[0] + 1,self.position[1] + 1] 
            ]

    #TODO movimentação. Altera a posição
