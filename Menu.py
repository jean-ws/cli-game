import WConio2
import cursor

class Menu:
    def __init__(self,width,height):
        self.frameWidth = width
        self.frameHeight = height
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        WConio2.textcolor(14) #14 = yellow

    def _borderUpDown(self):
        print('█' + '█' * self.frameWidth + '█')

    def _drawLeftBorder(self,number_of_spaces):
        print('██' + '  ' * number_of_spaces, end = '')

    def _drawRightBorder(self,number_of_spaces):
        print('  ' * number_of_spaces + '██')

    def _drawBlankLines(self,number_of_lines):
        for line in range(number_of_lines):
            print('██' + (' ' * (self.frameWidth-2)) + '██')

    def _drawRunBro(self):
    
        self._drawLeftBorder(5) 
        print('  ' * 10 + '██' * 3  + '  ' * 2  + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1, end = ' ') 
        self._drawRightBorder(17)

        self._drawLeftBorder(5) 
        print('  ' * 10 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 2 + '  ' * 1 + '██' * 1, end = ' ')
        self._drawRightBorder(17)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 3 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 2 , end = ' ')
        self._drawRightBorder(17)
        
        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 1 + '  '* 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 , end = ' ')
        self._drawRightBorder(17)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 2 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + ' ' * 1 + '██' * 1, end = '  ')
        self._drawRightBorder(15)

        self._drawLeftBorder(0)
        print( '  ' * 30 + '█' * 1, end = '  ')
        self._drawRightBorder(15)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 3 + '  ' * 2 + '██' * 3 + '  ' * 3 + '██' * 2 + '  ' * 1 , end = ' ')
        self._drawRightBorder(17)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 , end = ' ')
        self._drawRightBorder(17)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 3 + '  ' * 2 + '██' * 3 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 , end = ' ')
        self._drawRightBorder(17)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 1 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 , end = ' ')
        self._drawRightBorder(17)

        self._drawLeftBorder(5)
        print('  ' * 10 + '██' * 3 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 1 + '  ' * 2 + '██' * 2 + '  ' * 1 , end = ' ')
        self._drawRightBorder(17)
    
    def _drawInputs(self):

        self._drawLeftBorder(0)
        print(' '* 31 + "Press [SPACE] for a new game: ", end = '')
        self._drawRightBorder(16)

        self._drawLeftBorder(0)
        print(' '* 31 + "Press [R] for the recors: ", end = '  ')
        self._drawRightBorder(17)

    def _drawMadeBy(self):
        self._drawLeftBorder(0)
        print(' '* 42 + "Made by: ")
        self._drawRightBorder(48)

        self._drawLeftBorder(0)
        print(' '* 31 + "jean-ws, Mo0inha, buno, gabs")
        self._drawRightBorder(48)


    def drawScreen(self):
        WConio2.gotoxy(0,0)
        self._borderUpDown()
        self._drawBlankLines(2)

        self._drawRunBro()
        self._drawBlankLines(4)

        self._drawInputs()
        self._drawBlankLines(4)

        self._drawMadeBy()

        self._drawBlankLines(2)
        self._borderUpDown()

menu = Menu(95,40)
menu.drawScreen()
