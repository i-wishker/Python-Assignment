# Initializing the board
def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Displaying the board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Who is the winner?
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # No winner
    return None

# Player's input
def take_turn(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter row number (0 to 2): "))
            col = int(input(f"Enter column number (0 to 2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Illegal move!! The cell is already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")

# Main game loop
def play_game():
    board = init_board()  # Changed this to init_board() to match the definition
    current_player = "X"
    
    while True:
        display_board(board)
        take_turn(current_player, board)
        
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for tie (no empty spaces left)
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            display_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Step 6: Run the game
if __name__ == "__main__":
    play_game()

    






    