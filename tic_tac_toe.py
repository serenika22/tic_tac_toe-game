import random
#intialization of board
def create_board():
    return [" " for _ in range(9)]

# Print the current state of the board
def print_board(board):
    print("\n| {} | {} | {} |\n| {} | {} | {} |\n| {} | {} | {} |\n".format(*board))

# Handle player moves
def player_move(board, icon):
    while True:
        try:
            choice = int(input(f"Player {1 if icon == 'X' else 2} ({icon}), enter your move (1-9): ").strip()) - 1
            if 0 <= choice < 9 and board[choice] == " ":
                board[choice] = icon
                break
            print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

# Check if a player has won
def is_victory(board, icon):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == icon for i in combination) for combination in winning_combinations)

# Check if the game is a draw
def is_draw(board):
    return " " not in board

# Main game loop with additional features
def play_game():
    # Score tracking
    scores = {"X": 0, "O": 0, "Draw": 0}
    while True:
        board = create_board()
        current_icon = random.choice(["X", "O"])  # Randomize starting player
        print(f"\n--- New Game! Player {1 if current_icon == 'X' else 2} ({current_icon}) starts ---")

        # Gameplay loop
        while True:
            print_board(board)
            player_move(board, current_icon)
            if is_victory(board, current_icon):
                print_board(board)
                print(f"Player {1 if current_icon == 'X' else 2} ({current_icon}) wins! Congratulations!")
                scores[current_icon] += 1
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                scores["Draw"] += 1
                break
            current_icon = "O" if current_icon == "X" else "X"  # Switch players

        # Display scores and ask if they want to play again
        print(f"\nScores:\nPlayer 1 (X): {scores['X']} wins\nPlayer 2 (O): {scores['O']} wins\nDraws: {scores['Draw']}")
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!Bye!")
            break

# Start the game
play_game()
