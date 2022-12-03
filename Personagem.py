class Personagem():
    #atributos que TODOS personagens (vilão e heroi) terão

    def __init__(self,icon,posicao,tamanho,velocidade):
        self.icon = icon #cada index na lista é uma linha
        self.posicao = posicao # [x, y]
        self.tamanho = tamanho #exemplo de tamanho 2x2
        self.velocidade = velocidade #quanto maior, menor deve ser o divisor ao dividir a cont
        pass
    

    #metodos
    def setPosicao(self,x,y):
        self.posicao[0] = x 
        self.posicao[1] = y

    #TODO não atravessa limite do mapa
    def is_out(self):
        
        return