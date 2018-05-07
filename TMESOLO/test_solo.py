from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy

GAME_WIDTH = 150
GAME_HEIGHT = 90
GAME_GOAL_HEIGHT = 10
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
maxPlayerSpeed = 1.
maxPlayerAcceleration = 0.2
playerBrackConstant = 0.1
nbWithoutShoot = 10
maxPlayerShoot = 6.
maxBallAcceleration = 6.
shootRandomAngle = 0.2
ballBrakeConstant = 0.06
ballBrakeSquare = 0.01
MAX_GAME_STEPS = 2000
PREC=4

class Outil(object):
	def __init__(self,state,team,player):
		self.state=state
		self.team=team
		self.player=player
############### Fonction de BASE ################
	def vitesse_ball(self):
		return self.state.ball.vitesse	

	def posi_ball(self):
		return self.state.ball.position

	def posi_player(self):
		return self.state.player_state(self.team,self.player).position 

	def dist_player_ball(self):
		return (self.posi_ball() - self.posi_player()).norm

	def vect_player_ball(self):
		return (self.posi_ball() - self.posi_player())

	def vect_player_posi(self,x,y):
		return Vector2D(x,y) - self.posi_player()

	def peut_tirer(self):
		if (self.dist_player_ball() < PLAYER_RADIUS + BALL_RADIUS):
			return True
		return False	


class FonceurLent(Strategy):
    def __init__(self):
        super(FonceurLent,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position)*(1/75)
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.8:
            return SoccerAction(Vector2D(0,0), shoot+ Vector2D(-0.05,0))
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=0.1
        return SoccerAction(acceleration=acc)


myt = SoccerTeam("prof")
myt.add("N",FonceurLent())
b = Billard(myt,type_game=1)
show_simu(b)

