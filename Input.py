class Input:
    def __init__(self,hero,hunter,width,height):
        self.hero = hero
        self.hunter = hunter
        self.frame_width = width
        self.frame_height = height
        self.border_limits = {
            'horizontal': {
                'left': 1,
                 'right': width-3
            },

            'vertical': {
                'left': 1,
                'right': height-1
            }
            }
    
    def getMove(self, key, character):
        #Hero normal movements
        if key != ' ':
            if character.position[0] not in self.border_limits['horizontal'].values() and character.position[1] not in self.border_limits['vertical'].values():
                #If the hero isn't in a border, only gets the movement
                movement = character.acceptedMoves[key]

            elif character.position[0] not in self.border_limits['horizontal'].values():
                #If hero is in a vertical border  
                if key in ['a','d','j','l']:
                    movement = character.acceptedMoves[key]
                else:
                    if key in ['w','i'] and character.position[1] != self.border_limits['vertical']['left']:
                        movement = character.acceptedMoves[key]

                    if key in ['s','k'] and character.position[1] != self.border_limits['vertical']['right']:
                        movement = character.acceptedMoves[key]
            
            else:
                #The hero is in a horizontal border
                if key in ['w','s','i','k']:
                    movement = character.acceptedMoves[key]
                else:
                    if key in ['a','j'] and character.position[1] != self.border_limits['horizontal']['left']:
                        movement = character.acceptedMoves[key]

                    if key in ['d','l'] and character.position[1] != self.border_limits['horizontal']['right']:
                        movement = character.acceptedMoves[key]

        #Hero teleports
        else:
            if character.last_move in ['a','j']:
                if self.position[0] - 8 >= 1:
                    movement = character._teleport
            
            if character.last_move in ['d','l']:
                if self.position[0] + 8 <= self.frame_width - 2:
                    movement = character._teleport
    
            if character.last_move in ['w','i']:
                if self.position[1] - 4 >= 1:
                    movement = character._teleport
            
            if character.last_move in ['s','k']:
                if self.position[1] + 4 <= self.frame_height - 2:
                    movement = character._teleport

        if key in self.hero.teleport:
            self.hero.last_move = key

        elif key in self.hunter.teleport:
            self.hunter.last_move = key

        return movement

    def verifyInput(self,key):
        #se for do heroi chama metodos que move heroi
        if key in self.hero.acceptedMoves:
            movement = self.getMove(key,self.hero)
            self.hero.move(movement)

        elif key in self.hunter.acceptedMoves:
            movement = self.getMove(key, self.hunter)
            self.hunter.move(movement)
