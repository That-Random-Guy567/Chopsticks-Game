from Game_Info import start_game, end_game
from function_def import (
    print_player_1_hands,
    print_player_2_hands,
    update_hand,
    print_hands,
    players,
    computer_move,
    format_hand
)

start_game()
print("---------------------")

while True:
    choice = input("Which hand would you like to attack WITH (user) (l/r): ").lower()
    attack = input("Which hand would you like to attack (opponent) (l/r): ").lower()

    # First, get which hand the player is attacking with
    if 'l' in choice:
        attacking_fingers = players["player1"]["left"]
    elif 'r' in choice:
        attacking_fingers = players["player1"]["right"]

    elif 'q' in attack or 'q' in choice:
        break

    else:
        print("Please Select a Valid Hand.")
        continue
#-------------------------------------
    # Then, update the opponent's hand that was attacked
    if 'l' in attack:
        new_value = players["player2"]["left"] + attacking_fingers
        update_hand("player2", "left", new_value)
    elif 'r' in attack:
        new_value = players["player2"]["right"] + attacking_fingers
        update_hand("player2", "right", new_value)

    elif 'q' in attack or 'q' in choice:
        break
    
    else:
        print("Please Select a Valid Hand.")
        continue

    print_hands()
    print("")
    print("---------------------")
    computer_move()
    print("")
    print_hands()
    print("")

end_game()
    