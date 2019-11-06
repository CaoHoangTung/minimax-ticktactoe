# THIS BOT TRACE ALL THE GAME STATES AND APPLY A SPECIFIC

# import Operator

# user = 1
# machine = 2


# class Bot():
#     def __init__(self,_game_size=3):
#         op = Operator.Operator()
#         self.game_size = _game_size
#         self.win_rate = op.zeros(_game_size, _game_size)
#         self.calculations = 0

#     def track_win_rate(self, _game, _i, _j, _player,_level):
#         self.calculations += 1
#         res = 0
#         _game.make_a_move(_i, _j, _player)

#         if _game.game_finished:
#             game_result = _game.game_result()
#             if game_result == 'machine wins':
#                 res = 1 + 1/(_level)
#             elif game_result == 'tie':
#                 res = 1/(_level)
#             else:
#                 res = -1 - 1/(_level)

#         new_player = machine if _player == user else user
        
        
#         for i in range(self.game_size):
#             for j in range(self.game_size):
#                 if _game.board[i][j] == 0:
#                     res += self.track_win_rate(_game,i,j,new_player,_level+1)

#         _game.undo_a_move()
#         return res

#     def calculate_win_rate(self, _game):
#         self.calculations = 0
#         subject = machine
#         for i in range(0, self.game_size):
#             for j in range(0, self.game_size):
#                 if _game.board[i][j] == 0:
#                     self.win_rate[i][j] = self.track_win_rate(_game, i, j, subject,1)
#                 else:
#                     self.win_rate[i][j] = -999999999999
#                 print("win_rate",i,j,"done")
#         print("WIN RATE:", self.win_rate)
#         return self.calculations

#     def max_win_rate(self):
#         max_rate = -999999999999
#         optimal_move = (-1, -1)
#         for i in range(0, self.game_size):
#             for j in range(0, self.game_size):
#                 if self.win_rate[i][j] > max_rate:
#                     max_rate = self.win_rate[i][j]
#                     optimal_move = (i, j)
#         return optimal_move

#     def make_decision(self, _game):
#         steps = self.calculate_win_rate(_game)
#         print(steps,"steps taken")
#         optimal_move = self.max_win_rate()
#         return optimal_move
