import random

# Initialize players' hands using a dictionary
players = {
    "player1": {"left": 1, "right": 1},
    "player2": {"left": 1, "right": 1},
}

def format_hand(fingers):
    return ''.join('|' if i < fingers else ' ' for i in range(4))

def print_player_1_hands():
    left_hand = format_hand(players["player1"]["left"])
    right_hand = format_hand(players["player1"]["right"])
    print("Yours:")
    print(f"[{left_hand}]    [{right_hand}]")

def print_player_2_hands():
    left_hand = format_hand(players["player2"]["left"])
    right_hand = format_hand(players["player2"]["right"])
    print("Opponent:")
    print(f"[{left_hand}]    [{right_hand}]")

def print_hands():
    print_player_1_hands()
    print_player_2_hands()

def update_hand(player, hand, value):
    players[player][hand] = value    # Sets new finger count
    if players[player][hand] >= 5:   # If fingers >= 5
        players[player][hand] = 0    # Hand "dies" (becomes 0)
    
# ------------------------------------------

def computer_move():
    # Choose a random active hand for computer
    valid_hands = []
    if players["player2"]["left"] > 0:
        valid_hands.append("left")
    if players["player2"]["right"] > 0:
        valid_hands.append("right")
    
    # If computer has no valid moves, return
    if not valid_hands:
        print("Computer has no valid moves!")
        return
    
    # Choose computer's hand and target
    comp_hand = random.choice(valid_hands)
    
    # Choose a valid target hand (player's hand)
    valid_targets = []
    if players["player1"]["left"] > 0:
        valid_targets.append("left")
    if players["player1"]["right"] > 0:
        valid_targets.append("right")
    
    if not valid_targets:
        print("No valid targets!")
        return
        
    target_hand = random.choice(valid_targets)
    
    # Calculate new value and update
    new_value = players["player1"][target_hand] + players["player2"][comp_hand]
    update_hand("player1", target_hand, new_value)
    print(f"Computer used {comp_hand} hand ({players['player2'][comp_hand]} fingers) "
          f"to tap your {target_hand} hand ({players['player1'][target_hand]} fingers)")