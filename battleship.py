#Made by Don and Paul
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(9):
    print ("Turn"), turn
    guess_row = int(input("Guess Row (0-4):"))
    guess_col = int(input("Guess Col (0-4):"))

    if guess_row == ship_row and guess_col == ship_col:
        print("bruh, you are an op. you missed the battleship.")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Nah fam. You should have known that's not even in the ocean...OP.")
        elif(board[guess_row][guess_col] == "X"):
            print("Fam, you guessed that one already. bruh.")
        else:
            print("bruh, you are an op. you missed the battleship.")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("Game Over")
        while True:
            answer = str(input('Do you wanna play again, fam? (yes/no): '))
            if answer in ('yes', 'no'):
                break
            print("Invaild input, please type the correct input.")
        if answer == 'yes':
            print_board(board)
        
        else:
            print("Bye op.")
            break
    turn =+ 1
    print_board(board)
