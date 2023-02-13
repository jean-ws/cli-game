class Score:
    def __init__(self):
        self.records = [100, 100, 100, 100, 100]
        self.scores = [ 100, 100, 100, 100, 100]
        self.currentScore = 0

    def verifyRecords(self):

        self.scores.append(self.currentScore)
        self.scores.sort(reverse=True)

        for i in range(5):
            self.records[i] = self.scores[i]
         
