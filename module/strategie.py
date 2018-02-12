from soccersimulator import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from .Outil import Outil
from soccersimulator.settings import *

## Fonceur sur la balle
class Fonceur(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")	
	def compute_strategy(self,state,id_team,id_player):
		outil = Outil(state, id_team, id_player)
		if (outil.peut_tirer()):
			if (id_team == 1):
				if (outil.posi_ball().x > (GAME_WIDTH*(3/4))):
					return outil.tir_bonne_precision()
				return outil.tir_mauvaise_precision()
			if (id_team == 2):
				if (outil.posi_ball().x < GAME_WIDTH*(1/4)):
					return outil.tir_bonne_precision()
				return outil.tir_mauvaise_precision()
		else:
			return outil.courir_vers_ball()
				

## Strategie aleatoire
class RandomStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
		return SoccerAction(Vector2D.create_random(-200,200),0)
		
## Fonceur intelligent
class Fonceur_intelligent(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")	
	def compute_strategy(self,state,id_team,id_player):
		if ((state.ball.position - state.player_state(id_team,id_player).position).norm < 50):
			outil = Outil(state, id_team, id_player)
			if (outil.peut_tirer()):
				if (id_team == 1):
					if (outil.posi_ball().x > (GAME_WIDTH*(3/4))):
						return SoccerAction(outil.vect_player_ball() ,(Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - outil.posi_ball())/3.5)
					return SoccerAction(outil.vect_player_ball() ,(Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - outil.posi_ball())/15)
				if (id_team == 2):
					if (outil.posi_ball().x < GAME_WIDTH*(1/4)):
						return SoccerAction(outil.vect_player_ball() ,(Vector2D(0,GAME_HEIGHT/2) - outil.posi_ball())/3.5)
					return SoccerAction(outil.vect_player_ball() ,(Vector2D(0,GAME_HEIGHT/2) - outil.posi_ball())/15)
			else:
				return SoccerAction(outil.vect_player_ball() ,0)
		else:
			return SoccerAction(0,0)
			
			
			
			
			
			
			
