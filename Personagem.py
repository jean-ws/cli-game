class Personagem:
    #atributos que TODOS personagens (vilão e heroi) terão

    def __init__(self,icon,posicao,velocidade):
        self.icon = icon #cada index na lista é uma linha
        self.posicao = posicao # [x, y]
        self.velocidade = velocidade #quanto maior, menor deve ser o divisor ao dividir a cont
        pass
    

    #metodos
    def _moveLeft(self):
        self.posicao[0] = self.posicao[0] - 1

    def _moveRight(self):
        self.posicao[0] = self.posicao[0] + 1

    def _moveUp(self):
        self.posicao[1] = self.posicao[1] - 1

    def _moveDown(self):
        self.posicao[1] = self.posicao[1] + 1

    #TODO não atravessa limite do mapa
    def is_out(self):
        pass