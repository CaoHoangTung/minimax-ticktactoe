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

    def game_result(self):
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