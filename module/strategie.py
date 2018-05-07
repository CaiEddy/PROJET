from soccersimulator import Strategy, SoccerAction, Vector2D,Billard
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from .Outil import Outil
from soccersimulator.settings import *

## STRATEGY

class tirAlea(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	
	def compute_strategy(self,state,id_team,id_player):
		outil = Outil(state, id_team, id_player)
		return outil.tirer_vers_la_balle()







			
