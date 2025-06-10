from function_def import ChopsticksGame

game = ChopsticksGame()

def start_game():
    print("---------------------")
    print("######## Welcome to Chopsticks ########")
    print("- Good luck!")
    print("- Type 'q' to quit. \n")
    game.print_hands()
    print("\n")

def end_game():
    print("")
    print("######## Thank you for playing ########")