#TODO altera o status pra False para sair do loop do jogo 
#verifica se alguma hitbox tocou em outra
class Status:
    def __init__(self):
        self.ingame = True
    
    def verifyCollisions(self,hero, enemy1):
        
        for hero_char in hero.hitbox:

            for enemy_char in enemy1.hitbox:
                
                if hero.hitbox[hero_char][0] == enemy1.hitbox[enemy_char][0] and hero.hitbox[hero_char][1] == enemy1.hitbox[enemy_char][1]:
                    self.ingame = False
                
