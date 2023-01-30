import WConio2
from Personagem import Personagem
#teste
class Heroi(Personagem):
    #método construtor
    def __init__(self):
        self.icon = ['██'] #2 caracteres █ que é 0 219 na ascii
        self.posicao = [25,15] #lista[x,y]
        self.velocidade = 3
        self.ultimo_movimento = ''

        #hitbox[char] == [x,y]
        self.hitbox = {
            'a' : self.posicao,
            'b' : [self.posicao[0] + 1, self.posicao[1]]
        }

        self.movimentosAceitados = {
        'a': self._moveLeft,
        'd': self._moveRight,
        'w': self._moveUp,
        's': self._moveDown,
        ' ': self._teleporte
        }

        #TODO dicionario com as funcoes teleporteUp, Down, etc (valores) de acordo com a ultima tecla pressionada (chaves) para nao precisar usar condicional no _teleporte()

    def _attHitbox(self):
        self.hitbox["a"] = [self.posicao]
        self.hitbox["b"] = [self.posicao[0]+1, self.posicao[1]]
            
    #TODO metodos teleporteUp, Down, etc 
    def _teleporte(self):
        #TODO trocar o match case pelo dicionario de funcoes de telporte quando o mesmo estiver pronto
        match self.ultimo_movimento:
            case 'a':
                self.posicao[0] = self.posicao[0] - 9
            case 'd':
                self.posicao[0] = self.posicao[0] + 9
            case 'w':
                self.posicao[1] = self.posicao[1] - 4
            case 's':
                self.posicao[1] = self.posicao[1] + 4

    def mover(self,movement):
        movement()
        self._attHitbox()

    #TODO def getHitbox():

    #TODO def getPosicao():