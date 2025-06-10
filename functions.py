from hand_counting_function import ChopsticksGame

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

def print_moves():
    game.print_hands()
    print("")
    print("---------------------")
    game.computer_move()
    print("")
    game.print_hands()
    print("")