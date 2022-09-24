# Tic Tac Toe Game
# @author Sayri Qunchiguango

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
current_player = "X"
winner = None
game_running = True



# Function for printing the Board
# @parameter board

def print_board(board):
   

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- + - + -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- + - + -")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# Function to take the player Input
# @parameter input
def player_input(board):
    input_1 = int(input(f"{current_player}'s turn to choose a square (1-9): "))
    if input_1 >= 0 and input_1 <=9: 
        if board[input_1 - 1] == str(input_1):
         board[input_1 - 1] = current_player
        else:
            print("Choose another one this place is occupied")
    else:
        print("The squares should be between 1-9")
        
# Function to check the winner Horizontals 
# @parameter board

def check_horizontals(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "1":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "4":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "7":
        winner = board[6]
        return True

# Function to check the winner Verticals 
# @parameter board
def check_verticals(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "1":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "2":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "3":
        winner = board[2]
        return True

# Function to check the winner Diagonals 
# @parameter board
def check_diagonals(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "1":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != "7":
        winner = board[6]
        return True


# Check if some player wins
def check_if_win(board):
    global game_running
    if check_horizontals(board):
        print_board(board)
        print(f'The winner is {winner}. Good game. Thanks for playing!')
        game_running = False
    elif check_verticals(board):
        print_board(board)
        print(f'The winner is {winner}. Good game. Thanks for playing!')
        game_running = False
    elif check_diagonals(board):
        print_board(board)
        print(f'The winner is {winner}. Good game. Thanks for playing!')
        game_running = False


# Switch Player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# System Controller
while game_running:
    print_board(board)
    player_input(board)
    switch_player()
    check_if_win(board)