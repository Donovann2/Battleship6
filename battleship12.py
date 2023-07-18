#Donovan Full Code

# ‘X’ indicates the ships hit

# ‘*‘ indicates the hits missed
from random import randint

Hidden_Pattern=[[' ']*5 for x in range(5)]
Guess_Pattern=[[' ']*5 for x in range(5)]

let_to_num={'1':0,'2':1, '3':2,'4':3,'5':4,}

def print_board(board):
    print('  1 2 3 4 5')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():

    #Enter the row number between 1 to 5
    row=input('Please enter a ship row 1-5 ').upper()
    while row not in '1 2 3 4 5':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-5 ')

    #Enter the Ship column from 1 to 5
    column=input('Please enter a ship column 1-5 ').upper()
    while column not in '12345':
        print("Please enter a valid column ")
        column=input('Please enter a ship column 1-5 ')
    return int(row)-1,let_to_num[column]

#Function that creates the ships
def create_ships(board):
    for ship in range(1):
        ship_r, ship_cl=randint(0,4), randint(0,4)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        board[ship_r][ship_cl] = 'X'



def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                new_func(count)
    return count

def new_func(count):
    count+=1

create_ships(Hidden_Pattern)

#print_board(Hidden_Pattern)
turns = 5
while turns > 0:
    print('Welcome to Battleship')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == '*':
        print(' You already guessed that stoopidd ')
    elif Hidden_Pattern[row][column] =='X':
        print(' Congratulations you have hit the battleship ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry,You missed')
        Guess_Pattern[row][column] = '*'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 1:
        print("Congratulations you have sunk my battleship ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')