def print_board(board):
    """Prints the current state of the game board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    """Checks if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    # Initialize a board with numbers 1-9 to show positions
    board = [str(i + 1) for i in range(9)]
    current_player = "X"
    moves = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while moves < 9:
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            
            if choice < 0 or choice > 8 or board[choice] in ["X", "O"]:
                print("Invalid move. Try again.")
                continue
            
            # Place the move
            board[choice] = current_player
            moves += 1
            print_board(board)

            # Check for win
            if check_win(board, current_player):
                print(f"Congratulations! Player {current_player} wins!")
                return

            # Switch players
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()