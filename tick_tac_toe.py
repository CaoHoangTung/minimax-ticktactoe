import Bot2
import Game 

user = 1
machine = 2

def user_make_a_move(game):
    while True:
        move = input("Make a move: ")
        indexi = int(move.split(' ')[0])
        indexj = int(move.split(' ')[1])
        if game.make_a_move(indexi,indexj,user):
            return (indexi,indexj)
        else:
            print("Input already taken. Try again")
    

def main():
    game = Game.Game()

    bot_turn = "first"

    bot = Bot2.Bot2(_game=game,_turn=bot_turn)
    bot.generate_states()
    while (not game.game_finished):
        if (bot_turn == "first"):
            bot_decision = bot.make_decision()
            print("bot go",bot_decision)
            game.make_a_move(bot_decision[0],bot_decision[1],machine)
            game.show_game_state()
            bot.update_tree_position(bot_decision)
            
            if game.game_finished:
                break  
            
            move = user_make_a_move(game)
            game.show_game_state()
            bot.update_tree_position(move)
        elif (bot_turn == "second"):
            move = user_make_a_move(game)
            game.show_game_state()
            bot.update_tree_position(move)
            
            if game.game_finished:
                break  
            
            bot_decision = bot.make_decision()
            print("bot go",bot_decision)
            game.make_a_move(bot_decision[0],bot_decision[1],machine)
            game.show_game_state()
            bot.update_tree_position(bot_decision)

    print(game.game_result())

main()

