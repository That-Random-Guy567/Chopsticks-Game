from functions import start_game, end_game, print_moves
from hand_counting_function import ChopsticksGame

game = ChopsticksGame()
start_game()

while True:
    choice = input("Which hand would you like to attack with (user) (l/r): ").lower()
    attack = input("Which hand would you like to attack (opponent) (l/r): ").lower()

    # First, get which hand the player is attacking with
    if 'l' in choice:
        attacking_fingers = game.players["player1"]["left"]
    elif 'r' in choice:
        attacking_fingers = game.players["player1"]["right"]
    elif 'q' in attack or 'q' in choice:
        break
    else:
        print("Please Select a Valid Hand.")
        continue

    # Then, update the opponent's hand that was attacked
    if 'l' in attack:
        new_value = game.players["player2"]["left"] + attacking_fingers
        game.update_hand("player2", "left", new_value)
    elif 'r' in attack:
        new_value = game.players["player2"]["right"] + attacking_fingers
        game.update_hand("player2", "right", new_value)
    elif 'q' in attack or 'q' in choice:
        break
    else:
        print("Please Select a Valid Hand.")
        continue

    print_moves()

end_game()