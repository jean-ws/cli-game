from random import randint
from Hero import Hero
from Enemy import *
import WConio2 #pip install WConio2
import cursor #pip install cursor

class Frame:
    def __init__(self,width,height):
        self.frameWidth = width
        self.frameHeight = height
        self.hero = Hero([randint(1,self.frameWidth-2),randint(1,self.frameHeight-2)])
        self.enemy1 = NormalEnemy([randint(1,self.frameWidth-2),randint(1,self.frameHeight-2)])
        self.char_background = ' '
        WConio2.clrscr()
        cursor.hide() 
        WConio2.textbackground(0)
        WConio2.textcolor(7)

    
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

        if characters_in_this_line["enemy1"]:
            if n_column == self.enemy1.hitbox['a'][0]:
                char = self.enemy1.icon[0][:1]
            elif n_column == self.enemy1.hitbox['b'][0]:
                char = self.enemy1.icon[0][1:]

        #TODO se tem que printar o enemy1
        #TODO o mesmo pros char de cada vilão

        return char


    def _drawLine(self,n_current_line):
        print('██', end = '')
    
        #TODO se vilao e heroi na mesma linha (IF ambos)
        #if self.enemy1.position[1] == self.linhaAtual or self.enemy1.hitbox[2][0] == self.linhaAtual:

        #TODO se vilao está na linha (ELIF vilao)
        #Se heroi está na linha (ELIF heroi - igual já está)
        characters_in_this_line = {
            'hero': False,
            'enemy1': False
        }

        if self.hero.position[1] == n_current_line:
            characters_in_this_line['hero'] = True
            
        if self.enemy1.position[1] == n_current_line:
            characters_in_this_line['enemy1'] = True

        if characters_in_this_line['hero'] or characters_in_this_line['enemy1']:
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
    
    def enemy1Move(self):
        self.enemy1.move(self.hero, self.frameWidth, self.frameHeight)
    
    def enemy2Move(self):
        self.enemy2.move(self.hero, self.frameWidth, self.frameHeight)
    
    def enemy3Move(self):
        self.enemy3.move(self.hero, self.frameWidth, self.frameHeight)

    def createEnemy2(self):
        self.enemy2 = NormalEnemy([randint(1,self.frameWidth-2),randint(1,self.frameHeight-2)])
    
    def createEnemy3(self):
        self.enemy3 = NormalEnemy([randint(1,self.frameWidth-2),randint(1,self.frameHeight-2)])

    def input(self,key):
        self.hero.move(key, self.frameWidth, self.frameHeight)
        if key in self.hero.teleport:
            self.hero.last_move = key