#Donovan Full Code

# ‘X’ indicates the ships hit

# ‘*‘ indicates the hits missed
from random import randint

Hidden_Pattern = [[' ']*7 for _ in range(7)]
Guess_Pattern = [[' ']*7 for _ in range(7)]

let_to_num={'1':0,'2':1, '3':2,'4':3,'5':4, '6':5, '7': 6}

def print_board(board):
    print('    1 2 3 4 5 6 7')
    row_num = 1
    for row in board:
        print(f"{row_num} | {'|'.join(row)}|")
        row_num += 1

def get_ship_location():
    while True:
        row = input('Please enter the ship row (1-7): ').strip().upper()
        column = input('Enter the ship column (1-7): ').strip().upper()
        if row in '1 2 3 4 5 6 7' and column in '1 2 3 4 5 6 7':
            return int(row) - 1, let_to_num[column]
        print('Enter valid row and column numbers.')
 

#Function that creates the ships
def create_ships(board):
    for _ in range(1):
        ship_r, ship_cl=randint(0,6), randint(0,6)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 6), randint(0, 6)
        board[ship_r][ship_cl] = 'X'



def count_hit_ships(board):
    return sum(row.count('X') for row in board)

def play_battleship():
    create_ships(Hidden_Pattern)
    
    turns = 5
    guesses = []
    while turns > 0:
        print('Welcome to Battleship')
        print_board(Guess_Pattern)
        row, column = get_ship_location()
        
        if (row, column) in guesses:
            print('You already guessed that.')
        elif Hidden_Pattern[row][column] == 'X':
            print('Congrats! You hit the battleship.')
            Guess_Pattern[row][column] == 'X'
            turns -= 1
        else:
            print('Sorry, you missed.')
            Guess_Pattern[row][column] = '*'
            turns -= 1
        
        guesses.append((row, column))
        
        if count_hit_ships(Guess_Pattern) == 1:
            print('Congrats. you sunk the battleship.')
            break
        
        print('You have', turns, 'turns remaining.')
        if turns == 0:
            print('The game is over.')
    
    return input('Do you wanna play again? (yes/no): ').lower() == 'yes'

def main():
    while True:
        if not play_battleship():
            print('Thanks for playing.')
            break

if __name__ == '__main__':
    main()