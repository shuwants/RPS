import random
moves = ['rock', 'paper', 'scissors']
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

PlayerA = RandomPlayer()
PlayerB = RandomPlayer()

def beats(one, two):
    return((one == "rock" and two == "scissors") or (one == "scissors" and two == "paper") or
    (one == "paper" and two == "rock"))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move(PlayerA)
        move2 = self.p2.move(PlayerB)
        print(f"Player 1: {move1}) Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")

if __name__ == "__main__":
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
