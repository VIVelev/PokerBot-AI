from pypokerengine.api.game import start_poker, setup_config

from bots.monte_carlo import MonteCarloBot
from bots.callbot import CallBot
import numpy as np

if __name__ == '__main__':
    blogger_bot = MonteCarloBot()

    # The stack log contains the stacks of the Data Blogger bot after each game (the initial stack is 100)
    stack_log = []
    for round in range(1000):
        p1, p2 = blogger_bot, CallBot()

        config = setup_config(max_round=5, initial_stack=100, small_blind_amount=5)
        config.register_player(name="p1", algorithm=p1)
        config.register_player(name="p2", algorithm=p2)
        game_result = start_poker(config, verbose=0)

        stack_log.append([player['stack'] for player in game_result['players'] if player['uuid'] == blogger_bot.uuid])
        print('Avg. stack:', '%d' % (int(np.mean(stack_log))))
