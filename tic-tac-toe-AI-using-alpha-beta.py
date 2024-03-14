import math

# Define the game class
class Game:
    def __init__(self):
        # Initialize an empty board
        self.board = [' ' for _ in range(9)]
        # No winner at the start
        self.current_winner = None

    # Print the current state of the board
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # Get the list of available moves
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # Check if there are empty squares left
    def empty_squares(self):
        return ' ' in self.board

    # Count the number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')

    # Make a move on the board
    def make_move(self, square, letter):
        # If the square is not occupied
        if self.board[square] == ' ':
            # Make the move
            self.board[square] = letter
            # Check if this move is a winning move
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Check if the current player has won
    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check the diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

# Function to play the game
def play(game, x_player, o_player, print_game=True):
    # Print the initial state of the board
    if print_game:
        game.print_board()
    # Start with player 'X'
    letter = 'X'
    # Game loop
    while game.empty_squares():
        # Get the move from the current player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # Make the move
        if game.make_move(square, letter):
            # Print the move
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')
            # Check if we have a winner
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # Switch to the other player
            letter = 'O' if letter == 'X' else 'X'
    # If we get here, it's a tie
    if print_game:
        print('It\'s a tie!')

# Define the player class
class Player:
    def __init__(self, letter):
        # Each player gets a letter ('X' or 'O')
        self.letter = letter

    # Get the player's move
    def get_move(self, game):
        pass

# Define the computer player class
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get the computer's move
    def get_move(self, game):
        # If it's the first move, choose randomly
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # Use the minimax algorithm to choose the best move
            square = self.minimax(game, self.letter)['position']
        return square

    # The minimax algorithm
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        # First, check if the previous move is a winning move
        if state.current_winner == other_player:
            return {'position': None, 'score': 1*(state.num_empty_squares()+1) if other_player == max_player else -1*(state.num_empty_squares()+1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        # Initialize the dictionary of moves
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        # Try every possible move
        for possible_move in state.available_moves():
            # Make the move
            state.make_move(possible_move, player)
            # Simulate the game after the move
            sim_score = self.minimax(state, other_player)
            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            # Update the dictionary of moves
            sim_score['position'] = possible_move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

# Define the human player class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get the human player's move
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

# Main function
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = Game()
    play(t, x_player, o_player, print_game=True)
