from profAI import ParamSearch
from profAI import FonceurTestStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from module.strategie import Fonceur
from module.strategie import Fonceur_brain_Test
from module.strategie import Fonceur_brain
from module.strategie import RandomStrategy
from module.strategie import Defenseur
from module.strategie import Defenseur_2v2
from module.strategie import Bon_joueur_1v1
from module.strategie import Bon_joueur_2v2


expe = ParamSearch(strategy=Fonceur_brain_Test(),
                   params={'CONSTANTE_A': [2,4,6,8,10,12,14,16,18,20],
			   'CONSTANTE_B': [25,30,35,40,45,50,55,60]},max_round_step=200)
expe.start()
print(expe.get_res())

