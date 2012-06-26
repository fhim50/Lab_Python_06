"""
Lab_Python_06
Part 1
"""
"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
import datetime
player_stats={'rooney':[(datetime.date(2012,6,23),2),(datetime.date(2012,5,25),2)],
              'ronaldo':[(datetime.date(2012,6,19),0),(datetime.date(2012,6,20),3)],
              'torres':[(datetime.date(2012,6,21),0),datetime.date(2012,6,21),1]}
#print player_stats
for k,v in player_stats.iteritems():
    print k ,v
#print player_stats.items()

print

## implement highest_score
score={'torres':1,'ronaldo':3,'ronney':4}
score_view= score.items()
#print score_view

print 'the highest score was ' ,map(max,zip(*score_view))[1]
 

print 
## implement highest_score_for_player
score={'ronney':[2,2],'ronaldo':[0,3],'torres':[0,1]}
for k,v in score.iteritems():
    print k,' highest score is ',max(v)



print zip(*score_view)
print max(zip(*score_view))

## implement highest_scorer
print
print map(min,zip(*score_view))[0]
#print max(zip(*score_view))
