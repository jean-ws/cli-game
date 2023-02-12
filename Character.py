class Character:
    #atributos que TODOS personagens (vilão e heroi) terão

    def __init__(self,icon,position,speed):
        self.icon = icon #cada index na lista é uma linha
        self.position = position # [x, y]
        self.last_move = ''
        self.teleport_lenght = [4,8]
        pass
    
    def _moveLeft(self):
        self.position[0] = self.position[0] - 1

    def _moveRight(self):
        self.position[0] = self.position[0] + 1

    def _moveUp(self):
        self.position[1] = self.position[1] - 1

    def _moveDown(self):
        self.position[1] = self.position[1] + 1

    def _attHitbox(self):
        self.hitbox["a"] = self.position
        self.hitbox["b"] = [self.position[0]+1, self.position[1]]
    
    def _teleportLeft(self):
        self.position[0] = self.position[0] - 8
    
    def _teleportRight(self):
        self.position[0] = self.position[0] + 8
    
    def _teleportUp(self):
        self.position[1] = self.position[1] - 4
    
    def _teleportDown(self):
        self.position[1] = self.position[1] + 4

    def _teleport(self):
        movement = self.teleport[self.last_move]
        movement()

    def move(self, movement):
        movement()
        self._attHitbox()