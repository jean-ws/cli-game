class Personagem():
    #atributos que TODOS personagens (vilão e heroi) terão

    #cada index na lista é uma linha
    icon = ['ÕÕ', 'µ '] 
    posicao = [30, 16] # [x, y]
    tamanho = [2,2] #exemplo de tamanho 2x2
    velocidade = 3 #quanto maior, menor deve ser o divisor ao dividir a cont

    #metodos
    def setPosicao(self,x,y):
        self.posicao[0] = x 
        self.posicao[1] = y
