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
			return outil.tir(id_team)
		else:
			return outil.courir_vers_ball()
				

## Strategie aleatoire
class RandomStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
		return SoccerAction(Vector2D.create_random(-200,200),0)
		
## Defenseur
class Defenseur(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")	
	def compute_strategy(self,state,id_team,id_player):
		outil = Outil(state, id_team, id_player)
		if (outil.ball_dans_rayon_but(id_team)):
			if (outil.peut_tirer()):
				return outil.defendre(id_team)
			return outil.courir_vers_ball()
		else:
			return outil.revenir_posi_def(id_team)
			
			
			
## Bon_joueur
	
class Bon_joueur(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")	
	def compute_strategy(self,state,id_team,id_player):
		outil = Outil(state, id_team, id_player)
		if (outil.peut_jouer()):
			if (outil.adversaire_devant_player_haut()):
				if (outil.peut_tirer()):
					return outil.tir_vers_milieu_bas()
				return outil.courir_vers_ball()
			if (outil.adversaire_devant_player_bas()):
				if (outil.peut_tirer()):
					return outil.tir_vers_milieu_haut()
				return outil.courir_vers_ball()
			
			else:
				if (outil.peut_tirer()):
					return outil.tir(id_team)
				else:
					return outil.courir_vers_ball()
		return outil.rien_faire()



















			
