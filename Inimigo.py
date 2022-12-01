from Personagem import Personagem

class Inimigo(Personagem):
    #atributos que TODOS inimigos terão
    pass

class InimigoNormal(Inimigo):
    #atributos que somente o inimigo normal terá
    hitbox = [[12,33],[13,33],[12,34],[13,34]]

    def __init__(self, icon, posicao, tamanho, velocidade):
        self.icon = icon #lista[linha de cima, linha de baixo]
        self.posicao = posicao #lista[x,y]
        self.tamanho = tamanho #lista[n,n] onde o tamanho é NxN
        self.velocidade = velocidade 
    pass
    
    #TODO metodo que altera posicao da hitbox. 

