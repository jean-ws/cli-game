import Heroi
import WConio2
import cursor #pip install cursor

class Tela:
    def __init__(self):
        self.tamanhoLateral = 50
        self.tamanhoVertical = 20
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(15)
        WConio2.textcolor(0)


    def _bordaCimaBaixo(self):
        print('-') *  self.tamanhoLateral

    def _verificaChar(self, heroi, n_linha_atual, n_char):

        char = self.char_background
                
        match n_char:

            #se é o PRIMEIRO caracter da PRIMEIRA linha do heroi
            case heroi.posicao[0]: 
                char = heroi.icon[0][:1]
            #se é o SEGUNDO caracter da PRIMEIRA linha do heroi
            case heroi.posicao[0] + 1: 
                char = heroi.icon[0][1:]
            #se é o PRIMEIRO caracter da SEGUNDA linha do heroi
            case heroi.hitbox[2][0]:
                char = heroi.icon[1][:1]
            #se é o SEGUNDO caracter da SEGUNDA linha do heroi
            case heroi.hitbox[3][0]:
                char = heroi.icon[1][1:]

            #TODO o mesmo pros char de cada vilão

        return char


    def _desenhaLinha(self,heroi,i1,i2,i3,i4,n_linha_atual):
        print('|', end = '')
    
        #TODO se vilao e heroi na mesma linha (IF ambos)
        #TODO se vilao está na linha (ELIF vilao)
        #Se heroi está na linha (ELIF heroi - igual já está)
        if heroi.posicao[1] == n_linha_atual or heroi.hitbox[2][0] == n_linha_atual:

            for n_char in range(self.tamanhoLateral):
                print(self._verificaChar(heroi,n_linha_atual,n_char), end = '')

        else:
            print(self.char_background * self.tamanhoLateral, end = '')
            
        print('|')       

        

    def _desenhaLinhas(self,heroi,i1,i2,i3,i4):
        self._desenhaLinha(heroi,i1,i2,i3,i4)

    def desenhaTela(self,heroi,i1,i2,i3,i4):
        WConio2.gotoxy(0,0)
        self._bordaCimaBaixo()
        self._desenhaLinhas(heroi,i1,i2,i3,i4)
