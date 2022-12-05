from Heroi import Heroi
from Inimigo import *
import WConio2 #pip install WConio2
import cursor #pip install cursor

class Tela:
    def __init__(self):
        #TODO criação dos objetos (heroi e inimigos)
        self.heroi = Heroi(['XX', 'xx'],[30,16],3)

        self.tamanhoLateral = 50
        self.tamanhoVertical = 20
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(15)
        WConio2.textcolor(0)

    
    def _bordaCimaBaixo(self):
        print('-') *  self.tamanhoLateral

    def _getChar(self, n_char):

        char = self.char_background 

        if n_char == self.heroi.hitbox2['a'][0]:
            char = self.heroi.icon[0][:1]
        elif n_char == self.heroi.hitbox['b'][0]:
            char = self.heroi.icon[0][1:]
        elif n_char == self.heroi.hitbox2['c'][0]:
            char = self.heroi.icon[1][:1]
        elif n_char == self.heroi.hitbox2['d'][0]:
            char = self.heroi.icon[1][1:]

        """
        match n_char:
            #se é o PRIMEIRO caracter da PRIMEIRA linha do heroi
            case self.heroi.hitbox[0][0] : 
                char = self.heroi.icon[0][:1]
            #se é o SEGUNDO caracter da PRIMEIRA linha do heroi
            case self.heroi.hitbox[1][0]: 
                char = self.heroi.icon[0][1:]
            #se é o PRIMEIRO caracter da SEGUNDA linha do heroi
            case self.heroi.hitbox[2][0]:
                char = self.heroi.icon[1][:1]
            #se é o SEGUNDO caracter da SEGUNDA linha do heroi
            case self.heroi.hitbox[3][0]:
                char = self.heroi.icon[1][1:]
            case _:
                print('default')

            #TODO o mesmo pros char de cada vilão
        """

        return char


    def _desenhaLinha(self,n_linha_atual):
        print('|', end = '')
    
        #TODO se vilao e heroi na mesma linha (IF ambos)
        #TODO se vilao está na linha (ELIF vilao)
        #Se heroi está na linha (ELIF heroi - igual já está)
        if self.heroi.posicao[1] == n_linha_atual or self.heroi.hitbox[2][0] == n_linha_atual:

            for n_char in range(self.tamanhoLateral):
                print(self._getChar(n_char), end = '')

        else:
            print(self.char_background * self.tamanhoLateral, end = '')
            
        print('|')       
        

    def _desenhaLinhas(self):
        self._desenhaLinha()


    def desenhaTela(self):
        WConio2.gotoxy(0,0)
        self._bordaCimaBaixo()
        self._desenhaLinhas()
