
#slip2_2
#write a computer program to play tic-tac-toe game.(Game Theory)
# Initialize the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Function to print the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Validate input
    while position not in [str(i) for i in range(1, 10)]:
        position = input("Invalid input. Choose a position from 1-9: ")

    position = int(position) - 1

    # Check if position is already taken
    while board[position] != "-":
        position = int(input("Position already taken. Choose a different position (1-9): ")) - 1

    board[position] = player
    print_board()

# Function to check if the game is over
def check_game_over():
    # Check for win conditions
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"

# Main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False

    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()

        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
