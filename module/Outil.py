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
	def vect_player_posi(self,x,y):
		return Vector2D(x,y) - self.posi_player()

	def revenir_posi_def(self,id_team):
		if (id_team == 1):
			return SoccerAction(self.vect_player_posi((GAME_WIDTH)*1/8,(GAME_HEIGHT)*1/2),0)
		if (id_team == 2):
			return SoccerAction(self.vect_player_posi((GAME_WIDTH)*7/8,(GAME_HEIGHT)*1/2),0)
		
	
	def ball_dans_rayon_but(self, id_team):
		if (id_team == 1):
			return self.posi_ball().x < (GAME_WIDTH)*3/8
		return self.posi_ball().x > (GAME_WIDTH)*5/8


	def defendre(self, id_team):
		return SoccerAction(self.vect_player_ball(),self.renvoyer_ball(id_team))

	def renvoyer_ball(self, id_team):
		if (id_team ==1):
			return self.vect_player_posi(GAME_WIDTH,GAME_HEIGHT)
		return self.vect_player_posi(0,GAME_HEIGHT)

	def bonne_precision_team1(self):
		return (Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - self.posi_ball())/3.5
	def mauvaise_precision_team1(self):
		return (Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - self.posi_ball())/15


	def bonne_precision_team2(self):
		return (Vector2D(0,GAME_HEIGHT/2) - self.posi_ball())/3.5
	def mauvaise_precision_team2(self):
		return (Vector2D(0,GAME_HEIGHT/2) - self.posi_ball())/15


	def tir_bonne_precision_team1(self):
		return SoccerAction(self.vect_player_ball(),self.bonne_precision_team1())
	def tir_mauvaise_precision_team1(self):
		return SoccerAction(self.vect_player_ball(),self.mauvaise_precision_team1())


	def tir_bonne_precision_team2(self):
		return SoccerAction(self.vect_player_ball(),self.bonne_precision_team2())
	def tir_mauvaise_precision_team2(self):
		return SoccerAction(self.vect_player_ball(),self.mauvaise_precision_team2())


	def tir(self, id_team):
		if (id_team == 1):
			if (self.posi_ball().x > (GAME_WIDTH*(3/4))):
				return self.tir_bonne_precision_team1()
			return self.tir_mauvaise_precision_team1()
		if (id_team == 2):
			if (self.posi_ball().x < GAME_WIDTH*(1/4)):
				return self.tir_bonne_precision_team2()
			return self.tir_mauvaise_precision_team2()


	def courir_vers_ball(self):
		return SoccerAction(self.vect_player_ball(),0)


	def rien_faire(self):
		return SoccerAction(0,0)


	def posi_adversaire(self):
		idteam = 1 if self.team == 2 else 2
		return self.state.player_state(idteam,0).position

	def adversaire_devant_player_haut(self):
		if (self.posi_player().x < self.posi_adversaire().x):
			if (self.posi_player().y < self.posi_adversaire().y):
				return True
		return False

	def adversaire_devant_player_bas(self):
		if (self.posi_player().x < self.posi_adversaire().x):
			if (self.posi_player().y > self.posi_adversaire().y):
				return True
		return False

	def tir_vers_milieu_bas(self):
		return SoccerAction(self.vect_player_ball(), (Vector2D((GAME_WIDTH)*1/2,(GAME_HEIGHT)*3/4) - self.posi_ball())/60)

	def tir_vers_milieu_haut(self):
		return SoccerAction(self.vect_player_ball(), (Vector2D((GAME_WIDTH)*1/2,(GAME_HEIGHT)*1/4) - self.posi_ball())/60)



	def peut_jouer(self):
		if (self.dist_player_ball() < 50):
			return True
		return False



















