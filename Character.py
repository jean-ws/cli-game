class Character:
    #atributos que TODOS personagens (vilão e heroi) terão

    def __init__(self,icon,position,speed):
        self.icon = icon #cada index na lista é uma linha
        self.position = position # [x, y]
        self.speed = speed #quanto maior, menor deve ser o divisor ao dividir a cont
        pass
    

    #metodos
    def _moveLeft(self):
        self.position[0] = self.position[0] - 1

    def _moveRight(self):
        self.position[0] = self.position[0] + 1

    def _moveUp(self):
        self.position[1] = self.position[1] - 1

    def _moveDown(self):
        self.position[1] = self.position[1] + 1

    #TODO não atravessa limite do mapa
    def isOut(self):
        pass