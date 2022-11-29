from Personagem import Personagem

class Inimigo(Personagem):
    #atributos que TODOS inimigos terão
    pass

class InimigoNormal(Inimigo):
    #atributos que somente o inimigo normal terá
    hitbox = [[12,33],[13,33],[12,34],[13,34]]

    def __init__(self, nome, icon, velocidade, posicao):
        self. nome = 
        self.velocidade = velocidade
    pass

