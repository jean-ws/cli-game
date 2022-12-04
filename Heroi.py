import WConio2
from Personagem import Personagem
#teste
class Heroi(Personagem):
    #método construtor
    def __init__(self, icon, posicao, velocidade):
        self.icon = icon #lista[linha de cima, linha de baixo]
        self.posicao = posicao #lista[x,y]
        self.velocidade = velocidade
        self.ultimo_movimento = ''
        self.hitbox = [
            [self.posicao], #char principal
            [self.posicao[0] + 1, self.posicao[1]], 
            [self.posicao[0], self.posicao[1] + 1], 
            [self.posicao[0] + 1,self.posicao[1] + 1]
            ]
        #hitbox[char][x]
        self.hitbox2 = {
            'a' : self.posicao,
            'b' : [self.posicao[0] + 1, self.posicao[1]],
            'c' : [self.posicao[0], self.posicao[1] + 1],
            'd' : [self.posicao[0] + 1,self.posicao[1] + 1]
        }

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
                self.posicao[1] = self.posicao[1] - 4
            case 's':
                self.posicao[1] = self.posicao[1] + 4
    
    def _alteraHitbox(self):
        self.hitbox = [
            [self.posicao], #char principal
            [self.posicao[0] + 1, self.posicao[1]],
            [self.posicao[0], self.posicao[1] + 1], 
            [self.posicao[0] + 1,self.posicao[1] + 1] 
            ]
        
    def alteraPosicao():
        pass

    #TODO def getHitbox():

    #TODO def getPosicao():