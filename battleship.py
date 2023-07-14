#Made by Don and Paul
import random

# This area right here....is to create the board.
def create_board():
    board = []
    for _ in range(5):
        board.append(["O"] * 5)
    return board

#This area right here.....is to print the game board.
def print_board(board):
    for row in board:
        print((" ").join(row))

#This area right here fam......is to place the battleships on the board.
def place_battleships(board):
    for _ in range(3):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        board[row][col] = "O"

#This right here fam....is to get user's guess and check 
def guess_ship(board):
    while True:
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Row (0-4): "))
        if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print("Nah fam. You should have known that's not even in the ocean...OP.")
        elif board[guess_row][guess_col] == "X":
            print("Bro, you guessed that one already. bruh")
        else:
            break

    if board[guess_row][guess_col] == "O":
        print("Congrats fam. you sunk the battleship.")
        board[guess_row][guess_col] = "X"
        return True
    else:
        print("bruh, you are an op. you missed the battleship.")
        board[guess_row][guess_col] = "X"
        return False

#This right here fam....is to play the game....NERD
def play_battleship():
    print("Let's play some battleship...or whatever fam.....")
    board = create_board()
    place_battleships(board)
    print_board(board)
    
    while True:
        if guess_ship(board):
            print_board(board)
            play_again = input("fam, do you want to play again bruh? (yes/no): ")
            if play_again.lower() == "no":
                print("thanks for playing fam. bye op.")
                break
            else:
                board = create_board()
                place_battleships(board)
                print_board(board)
        else:
            print_board(board)

play_battleship()
    


