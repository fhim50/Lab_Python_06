class Player:
    def __init__(self,firstname,lastname,team):
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
    
class Team:
  def __init__ (self,name,league,manager_name,points):
    self.name=name
    self.league=league
    self.manager=manager_name
    self.point=points
    self.players=[]
    
  def add_player(self,player):
    self.players.append(player)
    return self.players
  def __str__(self):
    team = self.name,' plays ',self.league,'and managed by ',self.manager,'points are : ',self.point
    return team
portugal=Team('portugal','PPL','Sir Man',10)
spain = Team('spain','SPL','Sir Wan',11)
torres =Player('Fernando','Torres',spain.name)
ronaldo = Player( "Cristiano", "Ronaldo", portugal.name )
xavi=Player('Xavi','whoo',spain.name)
spain.add_player(torres)
spain.add_player(xavi)
portugal.add_player(ronaldo)



''''
for i in range(len(spain.players)):
  print spain.players[i]
print 'Players of portugal'
print portugal.players
'''
import datetime
class Match:
  def __init__(self,home_team,away_team,date= None ):
    self.home_team=home_team
    self.awaay_team=away_team
    self.date=0
    self.home_scores={}
    self.away_scores= {}
  
  def home_score(self):
    return sum(self.home_scores.values())
    '''for value in self.home_scores.itervalue():
      total=0
      total+=value
    return total
    '''
  def away_score(self):
    return sum(self.away_scores.values())
  
  def winner(self):
    if self.home_score() > self.away_score():
      return self.home_team
    
 
    return self.away_team

  def add_score(self,player,score):
    #self.home_scores[player]=score
    #return self.home_scores
    player_team=player.team
    if player_team == self.home_team:
      if player.last_name not in self.home_scores:
        self.home_scores[player.last_name] = score
      else:
        self.home_scores[player.last_name] += score
    else:
      if player.last_name not in self.away_scores:
        self.away_scores[player.last_name] = score
      else:
        self.away_scores[player.last_name] += score
    return None

euro_semi_finals =Match('spain','portugal',datetime.date(2012,6,27).__format__(''))
  
euro_semi_finals.add_score(torres,1)
euro_semi_finals.add_score(torres,1)
euro_semi_finals.add_score(ronaldo,1)
print 'winner ', euro_semi_finals.winner(),date.Match()
    

