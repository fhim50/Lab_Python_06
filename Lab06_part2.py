class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name= firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team
    def add_score(self,date,score):
        self.scores.append(score)
        return 
