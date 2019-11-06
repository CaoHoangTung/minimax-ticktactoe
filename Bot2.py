# 19683 game states

import Operator as op
import math
import Game 

user = 1
machine = 2

class Node():
    def __init__(self,_index,_value=0):
        self.index = _index
        self.value = _value
        self.childs = []
        self.move = (0,0)

    def __str__(self):
        return str((self.index,self.value,self.move))

class Tree():
    def __init__(self):
        self.nodes = [] # contains nodes
    
    def append_node(self,_node):
        self.nodes.append(_node)

class Bot2():
    def __init__(self,_turn="first",_game=None):
        self.simulation = Game.Game()
        self.tree = Tree()
        self.turn = _turn

        self.current_game_state = {
            "tree_index": 0,
        }
        self.game = _game

    def __build_tree(self,_minimizing,_level):
        index = len(self.tree.nodes)
        initial_node_value = 10 if _minimizing else -10
        node = Node(index,initial_node_value)
        self.tree.append_node(node)

        if self.simulation.game_finished:
            game_result = self.simulation.game_result()
            if game_result == "machine wins":
                if self.turn == "first": # if bot is maximizing
                    self.tree.nodes[index].value = 1
                else:
                    self.tree.nodes[index].value = -1

            elif game_result == "tie!":
                self.tree.nodes[index].value = 0
            else:
                if self.turn == "first": # if bot is maximizing
                    self.tree.nodes[index].value = -1
                else:
                    self.tree.nodes[index].value = 1
            return index

        for i in range(0,3):
            for j in range(0,3):
                player = machine 
                if (self.turn == "first" and _minimizing) or (self.turn == "second" and not _minimizing): 
                    # bot is maximizing and the current turn is minimizing or bot is minimizing and the current turn is maximizing
                    player = user

                if self.simulation.board[i][j] != 0:
                    continue
                # print("MOVE",i,j,player,self.turn,_minimizing,_level)
                self.simulation.make_a_move(i,j,player)
                new_node_index = self.__build_tree(_minimizing = not _minimizing, _level = _level+1)
                self.tree.nodes[new_node_index].index = new_node_index
                self.tree.nodes[new_node_index].move = (i,j)
                if _minimizing:
                    self.tree.nodes[index].value = min(self.tree.nodes[index].value,self.tree.nodes[new_node_index].value)
                else:
                    self.tree.nodes[index].value = max(self.tree.nodes[index].value,self.tree.nodes[new_node_index].value)
                
                self.tree.nodes[index].childs.append(new_node_index)

                self.simulation.undo_a_move()
                
        # self.simulation.show_game_state()
        # print(index,self.tree.nodes[index].value,self.tree.nodes[index].childs,self.alpha,self.beta)
        return index

    def generate_states(self): # build tree
        self.__build_tree(_minimizing = False, _level=0)
    
    def update_tree_position(self,move):
        current_tree_index = self.current_game_state["tree_index"]
        for i in self.tree.nodes[current_tree_index].childs:
            node = self.tree.nodes[i]
            if node.move == move:
                self.current_game_state["tree_index"] = node.index
                return

    def make_decision(self):
        # print(self.current_game_state["tree_index"])
        # print(self.tree.nodes[self.current_game_state["tree_index"]].childs)
        if (self.turn == "first"): # bot is maximizing
            # print("maximizing")

            optimal_point = -10
            optimal_move = (-1,-1)
            for index in self.tree.nodes[self.current_game_state["tree_index"]].childs:
                node = self.tree.nodes[index]
                if (self.game.board[node.move[0]][node.move[1]] != 0):
                    continue
                print(node)
                
                if optimal_point < node.value:
                    optimal_point = node.value
                    optimal_move = node.move
        else: # bot is minimizing
            # print("minimizing")
            optimal_point = 10 
            optimal_move = (0,0)
            
            for index in self.tree.nodes[self.current_game_state["tree_index"]].childs:
                node = self.tree.nodes[index]
                print(node)

                if (self.game.board[node.move[0]][node.move[1]] != 0):
                    continue
                if optimal_point > node.value:
                    optimal_point = node.value
                    optimal_move = node.move

        return optimal_move

# bot = Bot2()
# bot.generate_states()
# bot.test()
