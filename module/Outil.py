from soccersimulator import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from soccersimulator.settings import *


class Outil(object):
	def __init__(self,state,team,player,cst_force=5,cst_prediction):
		self.state=state
		self.team=team
		self.player=player
		self.cst_force=cst_force
		self.cst_prediction=cst_prediction
###fonction de base:		
	def goal_team(self):
		if (self.team == 1):
			return (0,GAME_HEIGHT/2)
		return (GAME_WIDTH, GAME_HEIGHT/2)
	def vitesse_ball(self):
		return self.state.ball.vitesse
	def posi_ball(self):
		return self.state.ball.position
	def posi_player(self):
		return self.state.player_state(self.team,self.player).position 
	def vitesse_player(self):
		return self.state.player_state(self.team,self.player).vitesse
	def dist_player_ball(self):
		return (self.posi_ball() - self.posi_player()).norm
	def vect_player_ball(self):
		return (self.posi_ball() - self.posi_player())
	def peut_tirer(self):
		me = state.player_state(1,0)
		if ((self.vitesse_ball().norm < 00.1) && (self.vitesse_player().norm <0.1)):
			if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
				return True
			return False
		return False
###Action:

	def tirer_vers_la_balle:
		if(self.peut_tirer()):
			return SoccerAction(self.state.balls[0].posi_ball()-self.posi_ball(),cst_force)

	def dist_adversaire_player(self,adversaire):
		return (self.vect_player_posi(adversaire.x,adversaire.y).norm)
		

	def vect_player_posi(self,x,y):
		return Vector2D(x,y) - self.posi_player()

	

	def prediction_ball(self):
		return self.vect_player_posi(self.predire_la_balle().x,self.predire_la_balle().y)


	def predire_la_balle(self):
		Constante = self.cst_prediction*self.dist_player_ball()
		return self.get_collision().a + Constante*self.vitesse_ball()

