import WConio2
import cursor

class GameOver:
    def __init__(self,width,height):
        self.frameWidth = width
        self.frameHeight = height
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        WConio2.textcolor(4)

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
        
        self._drawLeftBorder(self.frameWidth - 82) 
        print(' ' * 2 + '██' * 2  + '  ' * 3  + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4, end = ' ') 
        self._drawRightBorder(self.frameWidth - 82)

        self._drawLeftBorder(self.frameWidth - 82) 
        print('██' * 1 + ' ' * 8 + '██' * 1 + '  ' * 2 + '██' * 1 + ' ' * 2 + '██' * 2 + '  ' * 1 + '██' * 2 + '  ' * 1 + '██' * 1, end = ' ')
        self._drawRightBorder(self.frameWidth - 79)

        self._drawLeftBorder(self.frameWidth - 82)
        print('██' * 1 + ' ' * 2 + '██' * 2 + '  ' * 1 + '██' * 4 + ' ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 3, end = ' ')
        self._drawRightBorder(self.frameWidth - 81)
        
        self._drawLeftBorder(self.frameWidth - 82)
        print('██' * 1 + ' '* 4 + '██' * 1 + '  ' * 1 + '██' * 1 + ' ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 1, end = ' ')
        self._drawRightBorder(self.frameWidth - 79)

        self._drawLeftBorder(self.frameWidth - 82)
        print(' ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4, end = ' ')
        self._drawRightBorder(self.frameWidth - 82)

        self._drawBlankLines(2)

        self._drawLeftBorder(self.frameWidth - 82)
        print(' ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 4 + '  ' * 1 + '██' * 3, end = ' ')
        self._drawRightBorder(self.frameWidth - 81)

        self._drawLeftBorder(self.frameWidth - 82)
        print('██' * 1 + ' ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 3 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 4 + '██' * 1 + '  ' * 2 + '██' * 1, end = ' ')
        self._drawRightBorder(self.frameWidth - 82)

        self._drawLeftBorder(self.frameWidth - 82)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 3 + '  ' * 2 + '██' * 3, end = ' ')
        self._drawRightBorder(self.frameWidth - 81)

        self._drawLeftBorder(self.frameWidth - 82)
        print('██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 4 + '██' * 1 + '  ' * 1 + '██' * 1, end = ' ')
        self._drawRightBorder(self.frameWidth - 81)

        self._drawLeftBorder(self.frameWidth - 82)
        print('  ' * 1 + '██' * 2 + '  ' * 4 + '██' * 1 + '  ' * 3 + '██' * 4 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1, end = ' ')
        self._drawRightBorder(self.frameWidth - 82)
    
    def _drawScore(self,score):
        self._drawLeftBorder(0)

        if score.currentScore < 1000:
            print(' '* 25 + "Score:  ", score.currentScore, end = '')
        elif score.currentScore < 10000:
            print(' '* 25 + "Score: ", score.currentScore, end = '')
        elif score.currentScore < 100000:
            print(' '* 25 + "Score:", score.currentScore, end = '')
        else:
            print(' '* 25 + "Score:", '*****', end = '')
        self._drawRightBorder(28)

    def _drawRecord(self,score):
        self._drawLeftBorder(0)
        print(' '* 25 + "Records: ", end = ' ')
        self._drawRightBorder(29)

        
        self._drawLeftBorder(20)
        if score.records[0] < 1000:
            print( "TOP 1: ", score.records[0], end = '')
            self._drawRightBorder(21)
        elif score.records[0] < 10000:
            print( "TOP 1:", score.records[0], end = '')
            self._drawRightBorder(21)
        elif score.records[0] < 100000:
            print( "TOP 1:", score.records[0], end = '')
            self._drawRightBorder(20)
        else:
            print( "TOP 1:", 99999, end = '')
            self._drawRightBorder(20)

        self._drawLeftBorder(20)
        print( "TOP 2: ", score.records[1], end = '')
        self._drawRightBorder(21)

        self._drawLeftBorder(20)
        print( "TOP 3: ", score.records[2], end = '')
        self._drawRightBorder(21)
        
        self._drawLeftBorder(20)
        print( "TOP 4: ", score.records[3], end = '')
        self._drawRightBorder(21)

        self._drawLeftBorder(20)
        print( "TOP 5: ", score.records[4], end = '')
        self._drawRightBorder(21)

    def _drawMenu(self):
        self._drawLeftBorder(0)
        print(' '* 33 + "Press [SPACE] to continue ", end = '')
        self._drawRightBorder(17)

        self._drawLeftBorder(0)
        print('', end = ' ')
        self._drawRightBorder(46)

    def drawScreen(self,score):
        WConio2.gotoxy(0,0)
        self._borderUpDown()

        self._drawBlankLines(3)
        self._drawGameOver()
        self._drawBlankLines(3)

        self._drawScore(score)
        self._drawRecord(score)
        self._drawBlankLines(1)
        self._drawMenu()

        self._borderUpDown()
