import sys
sys.path.append('./Strategies')

from .strategies import RandomStrategy
from soccersimulator import SoccerTeam
from Strategie import Fonceur

def get_team(nb_players):
    myteam = SoccerTeam(name="MaTeam")
    if nb_players == 1:
        myteam.add("Joueur " ,Fonceur())
    if nb_players == 2:
	myteam.add("Joueur 1", Fonceur())
	myteam.add("Joueur 2", Fonceur())
    if nb_players == 4:
	myteam.add("Joueur 1",Fonceur())
	myteam.add("Joueur 2",Fonceur())
	myteam.add("Joueur 3",Fonceur())
	myteam.add("Joueur 4",Fonceur())
    return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),Fonceur())
	return myteam
