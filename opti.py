from profAI import ParamSearch
from profAI import FonceurTestStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from module.strategie import Fonceur
from module.strategie import RandomStrategy
from module.strategie import Defenseur
from module.strategie import Bon_joueur_1v1
from module.strategie import Bon_joueur_2v2


expe = ParamSearch(strategy=Fonceur(),
                   params={'force': [1/10,1/9,1/8,1/7,1/5]},max_round_step=50)
expe.start()
print(expe.get_res())

