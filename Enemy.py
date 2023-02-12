from Character import Character

#TODO classe de todos inimigos
class Enemy(Character):
    #atributos que TODOS inimigos terão
    pass

class NormalEnemy(Enemy):
    #atributos que somente o inimigo normal terá

    def __init__(self):
        self.icon = ["##","##"] #lista[linha de cima, linha de baixo]
        self.position = [2,10] #lista[x,y]
        self.speed = 3 
        self.acceptedMoves = {
            'x-': self._moveLeft,
            'x+': self._moveRight,
            'y-': self._moveUp,
            'y+': self._moveDown,
            }

        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]],
            'c' : [self.position[0], self.position[1] + 1],
            'd' : [self.position[0] + 1,self.position[1] + 1]
        }
    
    def _attHitbox(self):
        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]],
            'c' : [self.position[0], self.position[1] + 1],
            'd' : [self.position[0] + 1,self.position[1] + 1]
        }

    def trackHero():
        #TODO trackHero
        pass

    def move(self,hero,frame_width, frame_height):
        movement = 'x+' #TODO encaixar com o metodo trackHero
        action = self.acceptedMoves[movement]
        action(frame_width, frame_height)
        self._attHitbox()
        
    #TODO metodo que segue o heroi (usar velocidade)