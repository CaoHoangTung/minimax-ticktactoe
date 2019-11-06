import Bot
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
    game = Game.Game(_game_size=3,_to_win=3)
    # bot = Bot.Bot(_game_size=3)
    # while (not game.game_finished):
    #     user_make_a_move(game)
    #     game.show_game_state()
        
    #     if game.game_finished:
    #         break  
        
    #     bot_decision = bot.make_decision(game)
    #     # print("bot go",bot_decision)
    #     game.make_a_move(bot_decision[0],bot_decision[1],machine)
    #     game.show_game_state()

    #     print(game.game_result())

    bot = Bot2.Bot2(_game=game,_turn='second')
    bot.generate_states()
    while (not game.game_finished):

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

