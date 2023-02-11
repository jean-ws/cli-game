from Hero import *
from Hunter import *
from Input import *
import WConio2 #pip install WConio2
import cursor #pip install cursor

class Frame:
    def __init__(self):
        #TODO criação dos objetos (heroi e inimigos)
        self.hero = Hero()
        self.hunter = Hunter()
        self.keyboardInput = Input(self.hero, self.hunter)
        self.frameWidth = 100
        self.frameHeight = 40
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        WConio2.textcolor(4)

    
    def _borderUpDown(self):
        print('█' + '█' * self.frameWidth + '█')

    def _getChar(self, n_column,characters_in_this_line):

        char = self.char_background

        if characters_in_this_line['hero']:
            #se tem que printar o heroi
            if n_column == self.hero.hitbox['a'][0]:
                char = self.hero.icon[0][:1]
            elif n_column == self.hero.hitbox['b'][0]:
                char = self.hero.icon[0][1:]

        if characters_in_this_line["hunter"]:
            if n_column == self.hunter.hitbox['a'][0]:
                char = self.hunter.icon[0][:1]
            elif n_column == self.hunter.hitbox['b'][0]:
                char = self.hunter.icon[0][1:]
            elif n_column == self.hunter.hitbox['c'][0]:
                char = self.hunter.icon[1][:1]
            elif n_column == self.hunter.hitbox['d'][0]:
                char = self.hunter.icon[1][1:]

        #TODO se tem que printar o hunter
        #TODO o mesmo pros char de cada vilão

        return char


    def _drawLine(self,n_current_line):
        print('██', end = '')
    
        #TODO se vilao e heroi na mesma linha (IF ambos)
        #if self.hunter.position[1] == self.linhaAtual or self.hunter.hitbox[2][0] == self.linhaAtual:

        #TODO se vilao está na linha (ELIF vilao)
        #Se heroi está na linha (ELIF heroi - igual já está)
        characters_in_this_line = {
            'hero': False,
            'hunter': False
        }

        if self.hero.position[1] == n_current_line:
            characters_in_this_line['hero'] = True
            
        if self.hunter.position[1] == n_current_line or self.hunter.hitbox['c'][1] == n_current_line:
            characters_in_this_line['hunter'] = True

        if characters_in_this_line['hero'] or characters_in_this_line['hunter']:
            for n_column in range(1,self.frameWidth-1):
                print(self._getChar(n_column,characters_in_this_line), end = '')

        else:
            print(self.char_background * (self.frameWidth - 2), end = '')
            
        print('██')
        

    def _drawLines(self):
        for n_current_line in range(self.frameHeight):
            if n_current_line != 0 and n_current_line != self.frameHeight:
                self._drawLine(n_current_line)


    def drawFrame(self):
        WConio2.gotoxy(0,0)
        self._borderUpDown()
        self._drawLines()
        self._borderUpDown()
    
    def hunterMove(self):
        self.hunter.move(self.hero, self.frameWidth, self.frameHeight)

    def input(self,key):
        self.keyboardInput.verifyInput(key, self.frameWidth, self.frameHeight)

        '''
        self.hero.move(key, self.frameWidth, self.frameHeight)
        if key in self.hero.teleport:
            self.hero.last_move = key
        '''
