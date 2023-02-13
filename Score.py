#TODO classe que controla o score do jogo
#chamar no main
#aumentar a velocidade dos inimigos conforme o score aumenta

class Score:
    def __init__(self):
        self.record1 = 0
        self.record2 = 0
        self.record3 = 0
        self.record4 = 0
        self.record5 = 0
        self.currentScore = 0

    def verifyRecords(self,score):
        if score > self.record1:
            aux = self.record1
            self.record1 = score
            self.record2 = aux
            self.record3 = self.record2
            self.record4 = self.record3
            self.record5 = self.record4

        elif score > self.record2:
            aux = self.record2
            self.record2 = score
            self.record3 = aux
            self.record4 = self.record3
            self.record5 = self.record4

        elif score > self.record3:
            aux = self.record3
            self.record3 = score
            self.record4 = aux
            self.record5 = self.record4

        elif score > self.record4:
            aux = self.record4
            self.record4 = score
            self.record5 = aux

        elif score > self.record5:
            self.record5 = score