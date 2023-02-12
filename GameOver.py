import WConio2
import cursor

class GameOver:
    def __init__(self):
        self.frameWidth = 100
        self.frameHeight = 40
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        self.vermelho = 4
        self.roxo = 1
        pass

    def _borderUpDown(self):
        WConio2.textcolor(self.vermelho)
        print('█' + '█' * self.frameWidth + '█')


    def _drawBlankLine(self,n_current_line):
        
        WConio2.textcolor(self.vermelho)
        print('██', end = '')
        
        print(self.char_background * (self.frameWidth - 2), end = '')
        
        WConio2.textcolor(self.vermelho)
        print('██')

    def _drawGameOver(self,n_current_line):
        
        WConio2.textcolor(self.vermelho)
        print('██', end = '')
        
        WConio2.textcolor(self.roxo)
        print('██' * 5 + '  ' * 7 + '██' * 2)
        #TODO desenho do game over
        
        WConio2.textcolor(self.vermelho)
        print('██')
    
    def _drawScore():
        #TODO
        pass

    def _drawRecord():
        #TODO
        pass

    def _drawMenu():
        #TODO
        pass

    def _drawBlankLines(self):
        #TODO
        for n_current_line in range(self.frameHeight):
            if n_current_line != 0 and n_current_line != self.frameHeight:
                self._drawLine(n_current_line)


    def drawScreen(self):
        WConio2.gotoxy(0,0)
        self._borderUpDown()
        self._drawLines()
        self._borderUpDown()
    