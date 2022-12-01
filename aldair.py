import WConio2
from Personagem import Personagem

class Heroi(Personagem):
    #método construtor
    def __init__(self, icon, posicao, tamanho, velocidade):
        self.icon = icon #lista[linha de cima, linha de baixo]
        self.posicao = posicao #lista[x,y]
        self.tamanho = tamanho #lista[n,n] onde o tamanho é NxN
        self.velocidade = velocidade
        self.ultimo_movimento = ''
        #TODO hitbox. Pode ser uma lista com a posicao [x,y] de cada char do personagem

    def mover(self):
        (key, symbol) = WConio2.getch()
        self.ultimo_movimento = symbol

        match symbol:
            case 'a':
                self.posicao[0] = self.posicao[0] - 1
            case 'd':
                self.posicao[0] = self.posicao[0] + 1
            case 'w':
                self.posicao[1] = self.posicao[1] - 1
            case 's':
                self.posicao[1] = self.posicao[1] + 1
            case ' ':
                self._teleporte()
        
    def _teleporte(self):
        match self.ultimo_movimento:
            case 'a':
                self.posicao[0] = self.posicao[0] - 9
            case 'd':
                self.posicao[0] = self.posicao[0] + 9
            case 'w':
                self.posicao[1] = self.posicao[1] - 9
            case 's':
                self.posicao[1] = self.posicao[1] + 9
            case ' ':
                self._teleporte()

    pass
