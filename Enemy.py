from Character import Character

#TODO classe de todos inimigos
class Enemy(Character):
    #atributos que TODOS inimigos terão
    pass

class NormalEnemy(Enemy):
    #atributos que somente o inimigo normal terá

    def __init__(self,position):
        self.icon = ["██"] #lista[linha de cima, linha de baixo]
        self.position = position #lista[x,y]
        self.speed = 18 #the lower the number, the higher speed
        self.verticalMove = False
        self.acceptedMoves = {
            'x-': self._moveLeft,
            'x+': self._moveRight,
            'y-': self._moveUp,
            'y+': self._moveDown,
            }

        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]],
        }
    
    def _attHitbox(self):
        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]],
        }

    def trackHero(self,hero):
        
        if hero.position[0] > self.position[0]:
            movement = 'x+'
        elif hero.position[0] < self.position[0]:
            movement = 'x-'
        elif hero.position[1] > self.position[1]:
            movement = 'y+'
        elif hero.position[1] < self.position[1]:
            movement = 'y-'
        
        return movement

    def move(self,hero,frame_width, frame_height):
        movement = self.trackHero(hero)
        
        if movement[:1] == 'y': #slows verticals movements
            if self.verticalMove:
                self.verticalMove = False
            else:
                action = self.acceptedMoves[movement]
                action(frame_width, frame_height)
        else:
            action = self.acceptedMoves[movement]
            action(frame_width, frame_height)

        self._attHitbox()
        
    #TODO metodo que segue o heroi (usar velocidade)