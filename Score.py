#TODO classe que controla o score do jogo
#chamar no main
#aumentar a velocidade dos inimigos conforme o score aumenta

class Score:
    def __init__(self):
        self.records = [
            100,
            100,
            100,
            100,
            100
        ]
        self.aux = [
            100,
            100,
            100,
            100,
            100
        ]
        self.currentScore = 0

    '''    def attAux(self):
            aux = [
                self.records[0],
                self.records[1],
                self.records[2],
                self.records[3],
                self.records[4]
            ]
    '''
    def verifyRecords(self):

        aux = []
        for i in range(5):

            if self.currentScore > self.records[i]:
                
                for j in range(i):
                    aux.append(self.records[i])

                self.records[0] = self.currentScore

                for i in range(1,4):
                    self.records[i] = aux[(i-1)]
