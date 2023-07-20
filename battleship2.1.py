import random
#Made by Don and Paul

#This is when the board should start as 10x10.
while True:
    cole = False
    arrSize = 10
    try: 
        int(arrSize)
    except:
        print("Please provide an single number")
        cole = True
        continue
    if cole != True:
        if int(arrSize) > 10: 
            print('Come on now damn it')
            continue
    break
    
arr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]
myarr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]

#This is when you are choosing the row you are inputting.
while True:
    cole = False
    chooserR = input('Choose your Row: ')
    try:
        int(chooserR)
    except:
        print("Are you Dumb?")
        cole = True
        continue
    if cole != True:
        if int(chooserR) < 0 or int(chooserR) >= int(arrSize): #This is checking for out of bounds on row.
            print('Yeahhh i think you slow ben hawk')
            continue
    break

#This is when you are choosing the column you are inputting.
while True:
    cole = False
    chooserC = input('Choose Your Col: ')
    try:
        int(chooserC)
    except:
        print("Please provide a int -_-")
        cole = True
        continue
    if cole != True:
        if int(chooserC) < 0 or int(chooserC) >= int(arrSize): #This is checking for out of bounds on row.
            print('OH MY COME ONNNN!!!')
            continue
    break
myarr[int(chooserR)][int(chooserC)] = "H"


#This method that will print the opponent board.
def printBoard():
    print("The Oppositions")
    for r in range(len(arr)):
        print(arr[r])
        print()
        print(ship1.name)

#This will print the user's board.       
def printMyBoard():
    print("Your Board")
    for r in range(len(myarr)):
        print(myarr[r])
        print()
        print(ship2.name)

#This is to define the class of the ship. 
class ship:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
ship1 = ship("1", "1", "Chicago Bulls")
ship2 = ship("1", "1", "Lakers")


    

#This is storing the list of allMoves and allShips.
x = 0
row = random.randrange(0,int(arrSize))
col = random.randrange(0,int(arrSize))
print(str(col) + " , " + str(row))
allMoves = []
allShip = []



#This has something to do with the class of the ships.
allShip.append(ship1)
allShip.append(ship2)

#This will show you what round are you on.
while True:
    x += 1
    print("Round =", x)
    printBoard()

    #This is valadating the row input.
    while True:
        cole = False
        Trow = input('Choose Row: ')
        try:
            int(Trow)
        except:
            print("Please provide a int BENJAMIN")
            cole = True
            continue
        if cole != True:
            if int(Trow) < 0 or int(Trow) > 4: #This is checking for out of bounds on row.
                print('Please enter a number in the bounds.')
                continue
        break

    #This is valadating the col input.
    while True:
        cole = False
        Tcol = input('Choose Col: ')
        try:
            int(Tcol)
        except:
            print("Provide a Int BEN!")
            cole = True
            continue
        if cole != True:
            if int(Tcol) < 0 or int(Tcol) > 4: #This is checking for out of bounds on row.
                print('enter a number in the bounds.')
                continue
        break

    #This defines the hold on the row and col.
    hold = Trow
    Trow = Tcol
    Tcol = hold

    holder = False
    allMoves.append(int(Trow))
    allMoves.append(int(Tcol))
    if arr[int(Trow)][int(Tcol)] == "X":
        print("you have already did that Stooopiddd")
        x-=1 # This is subtracting 1 from the round number.
    else:
        remover = 0
        for i in range(len(allShip)):
            if int(allShip[i].x) == int(Trow) and int(allShip[i].y) == int(Tcol):
                print("You Hit Something at ", Tcol + " X, and at " + Trow + " Y")
                arr[int(Trow)][int(Tcol)] = "X"
                print("Ship Was Destoryed, You Win")
                quit()

#This code command is when you missed the target.
        if not holder:
            print("Miss!")
            arr[int(Trow)][int(Tcol)] = "X"
    attackR = random.randrange(0,int(arrSize))
    attackC = random.randrange(0,int(arrSize))
    while myarr[attackR][attackC] == "X":
        attackR = random.randrange(0,int(arrSize))
        attackC = random.randrange(0,int(arrSize))
    if myarr[attackR][attackC] == "H": #This code until line 170 means that you have been eliminated by the computer.
        myarr[attackR][attackC] = 'X'
        printMyBoard()
        print('You died.')
        quit()
    else:
        myarr[attackR][attackC] = 'X'
        printMyBoard()
        
    #if round is 5 or greater than 5 then the game is over and you lost.. loser...Nerd.
    if x >= 5:
        print("You have been eliminated hahahaha")
        quit()