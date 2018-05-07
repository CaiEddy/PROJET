from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from module.Outil import Outil
from module.strategie import *
from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy

class FonceurLent(Strategy):
    def __init__(self):
        super(FonceurLent,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position)*100
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
            return SoccerAction(shoot=shoot)
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=0.1
        return SoccerAction(acceleration=acc)

class tirAlea(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    
    def compute_strategy(self,state,id_team,id_player):
        outil = Outil(state, id_team, id_player)
        return outil.tirer_vers_la_balle()


myt = SoccerTeam("prof")
myt.add("N",FonceurLent())
b = Billard(myt,type_game=1)
show_simu(b)
