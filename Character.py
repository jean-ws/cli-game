class Character:
    #atributos que TODOS personagens (vilão e heroi) terão

    def __init__(self,icon,position,speed):
        self.icon = icon #cada index na lista é uma linha
        self.position = position # [x, y]
        self.speed = speed #quanto maior, menor deve ser o divisor ao dividir a cont
        pass
    
    def _moveLeft(self,frame_width, frame_height):
        self.position[0] = self.position[0] - 1

    def _moveRight(self,frame_width, frame_height):
        self.position[0] = self.position[0] + 1

    def _moveUp(self,frame_width, frame_height):
        self.position[1] = self.position[1] - 1

    def _moveDown(self,frame_width, frame_height):
        self.position[1] = self.position[1] + 1

    def _attHitbox(self):
        self.hitbox["a"] = self.position
        self.hitbox["b"] = [self.position[0]+1, self.position[1]]
    
    def _teleportLeft(self,frame_width,frame_height):
        if self.position[0] - 8 >= 1:
            self.position[0] = self.position[0] - 8
    
    def _teleportRight(self,frame_width,frame_height):
        if self.position[0] + 8 <= frame_width - 2:
            self.position[0] = self.position[0] + 8
    
    def _teleportUp(self,frame_width,frame_height):
        if self.position[1] - 4 >= 1:
            self.position[1] = self.position[1] - 4
    
    def _teleportDown(self,frame_width,frame_height):
        if self.position[1] + 4 <= frame_height - 2:
            self.position[1] = self.position[1] + 4
            
    def _teleport(self, frame_width, frame_height):
        teleport = self.teleport[self.last_move]
        teleport(frame_width,frame_height)

    def move(self, movement):
        movement()
        self._attHitbox()