import WConio2
import cursor

class GameOver:
    def __init__(self,width,height):
        self.frameWidth = width
        self.frameHeight = height
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        WConio2.textcolor(4)
        pass

    def _borderUpDown(self):
        print('█' + '█' * self.frameWidth + '█')

    def _drawLeftBorder(self,number_of_spaces):
        print('██' + '  ' * number_of_spaces, end = '')

    def _drawRightBorder(self,number_of_spaces):
        print('  ' * number_of_spaces + '██')

    def _drawBlankLines(self,number_of_lines):
        for line in range(number_of_lines):
            print('██' + (' ' * (self.frameWidth-2)) + '██')

    def _drawGameOver(self):
        
        self._drawLeftBorder(self.frameWidth - 80) 
        print(' ' * 2 + '██' * 2  + '  ' * 3  + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4, end = '') 
        self._drawRightBorder(self.frameWidth - 80)

        self._drawLeftBorder(self.frameWidth - 80) 
        print('██' * 1 + ' ' * 8 + '██' * 1 + '  ' * 2 + '██' * 1 + ' ' * 2 + '██' * 2 + '  ' * 1 + '██' * 2 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(self.frameWidth - 82)

        self._drawLeftBorder(self.frameWidth - 80)
        print('██' * 1 + ' ' * 2 + '██' * 2 + '  ' * 1 + '██' * 4 + ' ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 3, end = '')
        self._drawRightBorder(self.frameWidth - 84)
        
        self._drawLeftBorder(self.frameWidth - 80)
        print('██' * 1 + ' '* 4 + '██' * 1 + '  ' * 1 + '██' * 1 + ' ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(self.frameWidth - 82)

        self._drawLeftBorder(self.frameWidth - 80)
        print(' ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4, end = '')
        self._drawRightBorder(self.frameWidth - 80)

        self._drawBlankLines(2)

        self._drawLeftBorder(self.frameWidth - 80)
        print(' ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4 + '  ' * 1 + '██' * 3, end = '')
        self._drawRightBorder(self.frameWidth - 84)

        self._drawLeftBorder(self.frameWidth - 80)
        print('██' * 1 + ' ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 4 + '██' * 1 + '  ' * 2 + '██' * 1, end = '')
        self._drawRightBorder(self.frameWidth - 80)

        self._drawLeftBorder(self.frameWidth - 80)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 3 + '  ' * 2 + '██' * 3, end = '')
        self._drawRightBorder(self.frameWidth - 84)

        self._drawLeftBorder(self.frameWidth - 80)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1, end = '')
        self._drawRightBorder(self.frameWidth - 84)

        self._drawLeftBorder(self.frameWidth - 80)
        print('  ' * 1 + '██' * 2 + '  ' * 4 + '██' * 1 + '  ' * 3 + '██' * 4 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1, end = '')
        self._drawRightBorder(self.frameWidth - 80)
    
    def _drawScore(self):
        self._drawLeftBorder(0)
        print(' '* 14 + "Score: ", end = '')
        self._drawRightBorder(7)


    def _drawRecord(self):
        self._drawLeftBorder(0)
        print(' '* 14 + "Record: ", end = '')
        self._drawRightBorder(7)

    def _drawMenu(self):
        self._drawLeftBorder(0)
        print(' '* 18 + "Press [SPACE] to continue ", end = '')
        self._drawRightBorder(8)


    def drawScreen(self):
        WConio2.gotoxy(0,0)
        self._borderUpDown()

        self._drawBlankLines(3)
        self._drawGameOver()
        self._drawBlankLines(3)

        self._drawScore()
        self._drawRecord()
        self._drawMenu()

        self._borderUpDown()
