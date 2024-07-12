import random

class Board:
    def __init__(self, snakes, ladders):
        self.board_size = 100
        self.snakes = snakes
        self.ladders = ladders
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def move_player(self, player, steps):
        current_position = player.position
        new_position = current_position + steps
        if new_position > self.board_size:
            return  # Player stays in current position if exceeds board size
        if new_position in self.snakes:
            new_position = self.snakes[new_position]  # Move to snake tail
        elif new_position in self.ladders:
            new_position = self.ladders[new_position]  # Climb ladder
        player.position = new_position

    def has_player_won(self, player):
        return player.position == self.board_size

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  # Start from position 0
        self.winner = False

    def roll_dice(self):
        return random.randint(1, 6)

# Main game setup
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
board = Board(snakes, ladders)

# Add players
players = ["Player1", "Player2"]
for player_name in players:
    player = Player(player_name)
    board.add_player(player)

# Game loop
current_player_index = 0
while True:
    current_player = board.players[current_player_index]
    input(f"{current_player.name}'s turn. Press enter to roll the dice.")
    dice_roll = current_player.roll_dice()
    print(f"{current_player.name} rolled a {dice_roll}.")
    board.move_player(current_player, dice_roll)
    print(f"{current_player.name} is now at position {current_player.position}.")
    if board.has_player_won(current_player):
        print(f"{current_player.name} has won the game!")
        break
    current_player_index = (current_player_index + 1) % len(board.players)
