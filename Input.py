class Input:
    def __init__(self,hero,hunter):
        self.hero = hero
        self.hunter = hunter
        pass
    
    def getMove(self, key, frame_width, frame_height):
        if key == 'a' or 'j' and self.hero.position[0] != 1:
            if key == 'a': movement = self.hero.acceptedMoves[key]
            elif key == 'j': movement = self.hunter.acceptedMoves[key]

        elif key == 'd' or 'l' and self.hero.position[0] != frame_width - 3:
            if key == 'd': movement = self.hero.acceptedMoves[key]
            elif key == 'l': movement = self.hunter.acceptedMoves[key]

        elif key == 'w' or 'i' and self.hero.position[1] != 1:
            if key == 'w': 
                movement = self.hero.acceptedMoves[key]
            elif key == 'i': 
                movement = self.hunter.acceptedMoves[key]

        elif key == 's' or 'k' and self.hero.position[1] != frame_height - 1:
            if key == 's': movement = self.hero.acceptedMoves[key]
            elif key == 'k': movement = self.hunter.acceptedMoves[key]

        if key in self.hero.teleport:
            self.hero.last_move = key

        elif key in self.hunter.teleport:
            self.hunter.last_move = key

        return movement

    def verifyInput(self,key, frame_width, frame_height):
        #se for do heroi chama metodos que move heroi
        if key in self.hero.acceptedMoves:
            movement = self.getMove(key, frame_width, frame_height)
            self.hero.move(movement)

        elif key in self.hunter.acceptedMoves:
            movement = self.getMove(key, frame_width, frame_height)
            self.hunter.move(movement)
