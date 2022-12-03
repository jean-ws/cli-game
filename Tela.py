import Heroi
import WConio2
import cursor #pip install cursor

class Tela:
    def __init__(self):
        self.tamanhoLateral = 50
        self.tamanhoVertical = 20
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(15)
        WConio2.textcolor(0)


    def _bordaCimaBaixo(self):
        print('-') *  self.tamanhoLateral

    def _desenhaLinha(self,heroi,i1,i2,i3,i4):
        print('|', end = '')

        #TODO printar menos espaços na linha com o vilão
        #TODO if heroi.posicao[0] == i1.posicao[0]
        

    def _desenhaLinhas(self,heroi,i1,i2,i3,i4):
        self._desenhaLinha(heroi,i1,i2,i3,i4)

    def desenhaTela(self,heroi,i1,i2,i3,i4):
        WConio2.gotoxy(0,0)
        self._bordaCimaBaixo()
        self._desenhaLinhas(heroi,i1,i2,i3,i4)
