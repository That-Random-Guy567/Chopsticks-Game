import random

class ChopsticksGame:
    def __init__(self):
        self.players = {
            "player1": {"left": 1, "right": 1},
            "player2": {"left": 1, "right": 1},
        }

    def format_hand(self, fingers):
        return ''.join('|' if i < fingers else ' ' for i in range(4))

    def print_player_1_hands(self):
        left_hand = self.format_hand(self.players["player1"]["left"])
        right_hand = self.format_hand(self.players["player1"]["right"])
        print("Yours:")
        print(f"[{left_hand}]    [{right_hand}]")

    def print_player_2_hands(self):
        left_hand = self.format_hand(self.players["player2"]["left"])
        right_hand = self.format_hand(self.players["player2"]["right"])
        print("Opponent:")
        print(f"[{left_hand}]    [{right_hand}]")

    def print_hands(self):
        self.print_player_1_hands()
        self.print_player_2_hands()

    def update_hand(self, player, hand, value):
        self.players[player][hand] = value
        if self.players[player][hand] >= 5:
            self.players[player][hand] = 0

    def computer_move(self):
        valid_hands = [hand for hand in ["left", "right"] 
                      if self.players["player2"][hand] > 0]
        
        if not valid_hands:
            print("Computer has no valid moves!")
            return

        comp_hand = random.choice(valid_hands)
        
        valid_targets = [hand for hand in ["left", "right"] 
                        if self.players["player1"][hand] > 0]
        
        if not valid_targets:
            print("No valid targets!")
            return
            
        target_hand = random.choice(valid_targets)
        
        new_value = (self.players["player1"][target_hand] + 
                    self.players["player2"][comp_hand])
        self.update_hand("player1", target_hand, new_value)
        print(f"Computer used {comp_hand} hand ({self.players['player2'][comp_hand]} fingers) "
              f"to tap your {target_hand} hand ({self.players['player1'][target_hand]} fingers)")