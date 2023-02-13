import WConio2
import cursor



class GameOver:
    def __init__(self):
        self.frameWidth = 62
        self.frameHeight = 30
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

    def _drawLeftBorder(self,number_of_spaces):
        WConio2.textcolor(self.vermelho)
        print('██' + '  ' * number_of_spaces, end = '')

    def _drawRightBorder(self,number_of_spaces):
        WConio2.textcolor(self.vermelho)
        print('  ' * number_of_spaces + '██')

    def _drawBlankLine(self,n_current_line):
        
        WConio2.textcolor(self.vermelho)
        print('██', end = '')
        
        print(self.char_background * (self.frameWidth - 2), end = '')
        
        WConio2.textcolor(self.vermelho)
        print('██')

    def _drawGameOver(self):
        

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)
        
        self._drawLeftBorder(5) 
        print(' ' * 2 + '██' * 2  + '  ' * 3  + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4, end = '') 
        self._drawRightBorder(5)

        self._drawLeftBorder(5) 
        print('██' * 1 + ' ' * 8 + '██' * 1 + '  ' * 2 + '██' * 1 + ' ' * 2 + '██' * 2 + '  ' * 1 + '██' * 2 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(8)

        self._drawLeftBorder(5)
        print('██' * 1 + ' ' * 2 + '██' * 2 + '  ' * 1 + '██' * 4 + ' ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 3, end = '')
        self._drawRightBorder(6)
        
        self._drawLeftBorder(5)
        print('██' * 1 + ' '* 4 + '██' * 1 + '  ' * 1 + '██' * 1 + ' ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(8)

        self._drawLeftBorder(5)
        print(' ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4, end = '')
        self._drawRightBorder(5)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)


        self._drawLeftBorder(5)
        print(' ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4 + '  ' * 1 + '██' * 3, end = '')
        self._drawRightBorder(6)

        self._drawLeftBorder(5)
        print('██' * 1 + ' ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 4 + '██' * 1 + '  ' * 2 + '██' * 1, end = '')
        self._drawRightBorder(5)

        self._drawLeftBorder(5)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 3 + '  ' * 2 + '██' * 3, end = '')
        self._drawRightBorder(6)

        self._drawLeftBorder(5)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(6)

        self._drawLeftBorder(5)
        print('  ' * 1 + '██' * 2 + '  ' * 4 + '██' * 1 + '  ' * 3 + '██' * 4 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1, end = '')
        self._drawRightBorder(5)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)
        

    
    def _drawScore(self):
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

        self._drawLeftBorder(0)
        print(' '* 14 + "Score: ", end = '')
        self._drawRightBorder(7)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

    def _drawRecord(self):
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

        self._drawLeftBorder(0)
        print(' '* 14 + "Record: ", end = '')
        self._drawRightBorder(7)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

    def _drawMenu(self):
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

        self._drawLeftBorder(0)
        print(' '* 18 + "Press [SPACE] to continue ", end = '')
        self._drawRightBorder(8)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

    def _drawBlankLines(self):
        #TODO
        for n_current_line in range(self.frameHeight):
            if n_current_line != 0 and n_current_line != self.frameHeight:
                self._drawLine(n_current_line)



    def drawScreen(self):
        WConio2.gotoxy(0,0)
        self._borderUpDown()
        self._drawGameOver()
        self._drawScore()
        self._drawRecord()
        self._drawMenu()
        self._borderUpDown()

gover = GameOver()
gover.drawScreen()