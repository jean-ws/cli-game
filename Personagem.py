class Personagem():
    #atributos que TODOS personagens (vilão e heroi) terão

    #cada index na lista é uma linha
    icon = ['ÕÕ', 'µ '] 
    # ÕÕ
    # µ 

    posicao = {
        'x' : 30,
        'y' : 16
    }

    #exemplo de tamanho 2x2
    tamanho = [2,2]

    #metodos()
    def setPosicao(x,y):
        self.posicao['x'] = x 
        self.posicao['y'] = y