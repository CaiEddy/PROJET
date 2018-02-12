from soccersimulator import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from soccersimulator.settings import *


class Outil(object):
	def __init__(self,state,team,player):
		self.state=state
		self.team=team
		self.player=player
	def goal_team(self):
		if (self.team == 1):
			return (0,GAME_HEIGHT/2)
		return (GAME_WIDTH, GAME_HEIGHT/2)
	
	def posi_ball(self):
		return self.state.ball.position
	def posi_player(self):
		return self.state.player_state(self.team,self.player).position 
	def dist_player_ball(self):
		return (self.posi_ball() - self.posi_player()).norm
	def vect_player_ball(self):
		return (self.posi_ball() - self.posi_player())
	def peut_tirer(self):
		if (self.dist_player_ball() < PLAYER_RADIUS + BALL_RADIUS):
			return True
		return False
	def bonne_precision(self):
		return (Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - self.posi_ball())/3.5
	def mauvaise_precision(self):
		return (Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - self.posi_ball())/15
	def tir_bonne_precision(self):
		return SoccerAction(self.vect_player_ball(),self.bonne_precision())
	def tir_mauvaise_precision(self):
		return SoccerAction(self.vect_player_ball(),self.mauvaise_precision())
	def courir_vers_ball(self):
		return SoccerAction(self.vect_player_ball(),0)
	








































