class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name= firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team
        self.sum=0
        self.average= 0
    def add_score(self,date,score):
        self.scores.append(score)
        return self.scores

    def total_score(self):
        for scores in range(len(self.scores)):
            self.sum+=self.scores[scores]
        return self.sum
    def average_scores(self):
        self.total_score()
        newsum=float(self.sum)
        self.average = newsum/len(self.scores)
        return self.average
    
