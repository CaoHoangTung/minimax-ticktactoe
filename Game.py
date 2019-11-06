import Operator

user = 1
machine = 2

class Game():
    def __init__(self,_game_size=3, _to_win=3):
        op = Operator.Operator()
        self.game_size = _game_size
        self.board = op.zeros(_game_size,_game_size)
        self.to_win = _to_win
        self.move_made = 0
        self.game_finished = False
        self.moves = []
        self.direction_to_shift = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    
    def show_game_state(self):
        for i in range(0,self.game_size):
            output_line = ""
            for j in range(0,self.game_size):
                output_line += str(self.board[i][j]) + " "
            print(output_line,"\n")

    def make_a_move(self,_x,_y,_player):
        if not(0 <= _x < self.game_size and 0 <= _y < self.game_size) or self.board[_x][_y] != 0 :
            return False

        self.move_made += 1
        self.board[_x][_y] = _player

        if self.move_made == self.game_size**2 or self.game_result() != "tie!":
            self.game_finished = True
        self.moves.append((_x,_y))
        # print("   move:",_x,_y)
        return True

    def undo_a_move(self):
        last_move = self.moves.pop()
        self.board[last_move[0]][last_move[1]] = 0
        self.move_made -= 1
        self.game_finished = False
        return last_move

    # def __seek_winner(self,_position,_direction,_cur_step=0):
    #     # directions: 
    #     # 0 1 2 
    #     # 7 x 3
    #     # 6 5 4
    #     if self.board[_position[0]][_position[1]] == 0:
    #         return 0
    #     if _cur_step == self.to_win:
    #         return self.board[_position[0]][_position[1]]
        
    #     next_position = (_position[0]+self.direction_to_shift[_direction][0],
    #                      _position[1]+self.direction_to_shift[_direction][1])

    #     return self.__seek_winner(_position=next_position,_direction=_direction,_cur_step=_cur_step+1)

    def game_result(self):
        # winner = 0
        # for i in range(self.game_size):
        #     for j in range(self.game_size):
        #         for direction in range(8):
        #             temp_winner = self.__seek_winner(_position=(i,j),_direction=direction)
        #             if (temp_winner != 0):
        #                 winner = temp_winner
        #                 break
        
        # if winner == 0:
        #     return "tie!"
        # elif winner == user:
        #     return "you win"
        # elif winner == machine:
        #     return "machine wins"
        if (self.board[0] == [machine,machine,machine] or
            self.board[1] == [machine,machine,machine] or
            self.board[2] == [machine,machine,machine] or
            (self.board[0][0] == machine and self.board[1][0] == machine and self.board[2][0] == machine ) or
            (self.board[0][1] == machine and self.board[1][1] == machine and self.board[2][1] == machine ) or
            (self.board[0][2] == machine and self.board[1][2] == machine and self.board[2][2] == machine ) or
            (self.board[0][0] == machine and self.board[1][1] == machine and self.board[2][2] == machine ) or
            (self.board[0][2] == machine and self.board[1][1] == machine and self.board[2][0] == machine )
            ):
            return "machine wins"
        elif (self.board[0] == [user,user,user] or
            self.board[1] == [user,user,user] or
            self.board[2] == [user,user,user] or
            (self.board[0][0] == user and self.board[1][0] == user and self.board[2][0] == user ) or
            (self.board[0][1] == user and self.board[1][1] == user and self.board[2][1] == user ) or
            (self.board[0][2] == user and self.board[1][2] == user and self.board[2][2] == user ) or
            (self.board[0][0] == user and self.board[1][1] == user and self.board[2][2] == user ) or
            (self.board[0][2] == user and self.board[1][1] == user and self.board[2][0] == user )
            ):
            return "you win"
        else:
            return "tie!"