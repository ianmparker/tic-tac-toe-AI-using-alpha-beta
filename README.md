Try Beating this AI in Tic-Tac-Toe. It uses Minimax with Alpha-Beta Pruning to make decisions. Good Luck!

My LinkedIn : https://www.linkedin.com/in/ian-parker-596011142/

References:
MIT OpenCourseWare
Search: Games, Minimax, and Alpha-Beta
https://www.youtube.com/watch?v=STjW3eH0Cik&list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi&index=7

# tic-tac-toe-AI-using-alpha-beta

This code is an implementation of the Minimax algorithm, which is a decision-making algorithm used for finding the best move in games like tic-tac-toe, checkers, and chess. 

Overview:
---------
- Players: The code starts by identifying the maximum player (the one we are optimizing for) and the other player.
- Winning Move Check: It checks if the other player has won with their previous move. If so, it assigns a score to that game state. The score is positive if the other player is the max player and negative otherwise. The score is proportional to the number of empty squares plus one, which means the earlier the win, the higher the score.
- Draw Check: If there are no empty squares left and no one has won, it’s a draw, and the score is 0.
- Best Move Initialization: It initializes the best move and score. If the current player is the max player, it sets the score to negative infinity, and if it’s the other player, it sets the score to positive infinity.
- Move Simulation: For each possible move, it makes the move, simulates the game after the move by recursively calling the minimax function, and then undoes the move.
- Best Move Update: If the simulated score is better than the current best score, it updates the best move and score.
- Return Best Move: Finally, it returns the best move and its score. This best move is the one that the current player should take.
- This algorithm is based on the concept of optimization and recursion, and it assumes that both players are playing optimally.
- Identify Players: It sets up two players, one as the ‘max’ player who tries to maximize the score, and the other as the ‘min’ player who tries to minimize it.
- Check for Win or Draw: It checks if the game is already won by the last move or if it’s a draw (no empty spaces left).
- Best Move and Score: It initializes the best score and move for the current player. The best score is the worst possible score initially, so the algorithm can only improve from there.
- Explore Moves: It goes through all possible moves left in the game.
- Simulate Move: For each move, it simulates the game by making the move, calling itself to simulate the opponent’s move (recursion), and then undoing the move.
- Update Best Move: If the simulated move results in a better score than the current best, it updates the best move.
- The goal is to find the move that leads to the best possible outcome for the ‘max’ player, assuming the ‘min’ player is also playing optimally. The function returns the best move and its score.

![black child playing chess against ai 2](https://github.com/ianmparker/tic-tac-toe-AI-using-alpha-beta/assets/18231849/5774087c-5e50-490b-8fdf-da6a1a065c2f)
