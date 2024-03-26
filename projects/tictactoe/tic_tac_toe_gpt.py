def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board):
    """Checks if there is a winner."""
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
                board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " " or \
            board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def check_tie(board):
    """Checks if the game is a tie."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_on = True

    while game_on:
        print_board(board)

        # Get player's move
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("This spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers (0-2).")
            continue

        # Update board and check for win or tie
        board[row][col] = current_player
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_on = False
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            game_on = False
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

    # Ask if players want to play again
    if input("Play again? (y/n): ").lower() == "y":
        tic_tac_toe()

# Start the game
tic_tac_toe()
