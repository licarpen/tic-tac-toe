from tictactoe import player, actions, result, winner, terminal, utility, minimax

test_board = [['X', None,'O'], ['X', 'X', 'O'], ['O', None, None]]

print(minimax(test_board))