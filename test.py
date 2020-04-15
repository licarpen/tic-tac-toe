from tictactoe import player, actions, result, winner, terminal, utility

test_board = [['X', 'X', 'O'], ['O', 'O', 'O'], ['X', 'O', None]]

print(utility(test_board))