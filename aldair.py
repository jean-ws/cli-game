from Personagem import Personagem

class Heroi(Personagem):
    #método construtor
    def __init__(self, icon, posicao, tamanho, velocidade):
        self.icon = icon #lista[linha de cima, linha de baixo]
        self.posicao = posicao #lista[x,y]
        self.tamanho = tamanho #lista[n,n] onde o tamanho é NxN
        self.velocidade = velocidade 
    pass
