import WConio2
import cursor

class GameOver:
    def __init__(self):
        self.frameWidth = 95
        self.frameHeight = 40
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        self.vermelho = 14
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


    def _drawGameOver(self):
        

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)
        
        self._drawLeftBorder(5) 
        print('██' * 3  + '  ' * 2  + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1, end = '') 
        self._drawRightBorder(5)

        self._drawLeftBorder(5) 
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 2 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(8)

        self._drawLeftBorder(5)
        print('██' * 3 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 2 , end = '')
        self._drawRightBorder(6)
        
        self._drawLeftBorder(5)
        print('██' * 1 + '  '* 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 , end = '')
        self._drawRightBorder(8)

        self._drawLeftBorder(5)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + ' ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(5)

        self._drawLeftBorder(0)
        print(' ' * 39 + '█' * 1, end = '')
        self._drawRightBorder(30)

        self._drawLeftBorder(5)
        print('██' * 3 + '  ' * 2 + '██' * 3 + '  ' * 3 + '██' * 2 + '  ' * 1 , end = '')
        self._drawRightBorder(6)

        self._drawLeftBorder(5)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 , end = '')
        self._drawRightBorder(5)

        self._drawLeftBorder(5)
        print('██' * 3 + '  ' * 2 + '██' * 3 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 , end = '')
        self._drawRightBorder(6)

        self._drawLeftBorder(5)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 , end = '')
        self._drawRightBorder(6)

        self._drawLeftBorder(5)
        print('██' * 3 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 2 + '  ' * 1 , end = '')
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
        print(' '* 14 + "Press [SPACE] for a new game: ", end = '')
        self._drawRightBorder(7)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

    def _drawRecord(self):
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

        self._drawLeftBorder(0)
        print(' '* 14 + "Press [R] for the recors: ", end = '')
        self._drawRightBorder(7)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

    def _drawMenu(self):
        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

        self._drawLeftBorder(0)
        print(' '* 18 + "Made for us =D ", end = '')
        self._drawRightBorder(8)

        self._drawLeftBorder(0)
        print('', end = '')
        self._drawRightBorder(30)

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