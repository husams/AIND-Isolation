"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from sample_players import open_move_score

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        ##self.player1 = game_agent.MinimaxPlayer(search_depth=2, score_fn=open_move_score)
        #self.player2 = game_agent.MinimaxPlayer(search_depth=2, score_fn=open_move_score)

        self.player1 = game_agent.AlphaBetaPlayer(score_fn=open_move_score)
        self.player2 = game_agent.AlphaBetaPlayer(score_fn=open_move_score)
        self.game = isolation.Board(self.player1, self.player2, 9, 9)

    def test_minmax(self):
        #self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 22]
        winner, history, outcome = self.game.play()
        winner = "PLayer 1" if winner == self.player1 else "Player 2"
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))

    # def test_alphabeta(self):
    #     player1 = game_agent.AlphaBetaPlayer(search_depth=1, score_fn=open_move_score)
    #     player2 = game_agent.AlphaBetaPlayer(search_depth=1, score_fn=open_move_score)
    #     game = isolation.Board(player1, player2, 9, 9)
    #     game._board_state =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 62, 49]
    #     move, _ = player1.get_move(game, lambda : 10000)
    #     print("Move : {}".format(str(move)))
    #     print(game.to_string())

if __name__ == '__main__':
    unittest.main()
