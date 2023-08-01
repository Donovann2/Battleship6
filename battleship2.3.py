import random
#Cole has helped with the code!

#This is when the board should start as 10x10.

cole = False
arrSize = 10
    
    
arr = [["O" for i in range(int(10))] for i in range(int(10))]
myarr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]
EnemyArr = arr

def Func(row, col, size, dir):
    if dir == 0:
        try:
            for i in range(size):
                if EnemyArr[row+i][col] != "O":
                    return False
        except:
            return False
    else:
        try:
            for i in range(size):
                if EnemyArr[row][col+i] != "O":
                    return False
        except:
            return False
    return True

def add(row, col, size, dir, name):
    if dir == 0:
        for i in range(size):
            EnemyArr[row+i][col] = name
    else:
        for i in range(size):
            EnemyArr[row][col+i] = name

myShips = []
class Ship:
    def __init__(self,x,y):
        self.name = x
        self.list = y

cole = False
carrier = Ship("Carrier", [[0,0],[0,5]])
myShips.append(carrier)

battleship = Ship("Battleship", [[0,0],[0,4]])
myShips.append(battleship)

destroyer = Ship("Destroyer", [[0,0],[0,3]])
myShips.append(destroyer)

submarine = Ship("Submarine", [[0,0],[0,3]])
myShips.append(submarine)

patrol_boat = Ship("Patrol Boat", [[0,0],[0,2]])
myShips.append(patrol_boat)

for row in range(len(arr)):
    for col in range(len(arr[0])):
        print(row, col)
                     
            
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 5, dir):
        add(row, col, 5, dir, "B")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 4, dir):
        add(row, col, 4, dir, "G")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 3, dir):
        add(row, col, 3, dir, "L")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 3, dir):
        add(row, col, 3, dir, "Z")
        break
while True:
    row = random.randrange(0,10)
    col = random.randrange(0,10)
    dir = random.randrange(0,2) # 0 = vertical, 1 = horizontal
    if Func(row, col, 2, dir):
        add(row, col, 2, dir, "M")
        break
    

#This is when you are choosing the row you are inputting.
while True:
    cole = False
    myShipDir = input('Choose your ship direction (0 = vertical, 1 = horizontal): ')
    try:
        int(myShipDir)
    except:
        print("Try again.")
        cole = True
        continue
    if cole != True:
        if int(myShipDir) < 0 or int(myShipDir) >= 2: #This is checking for out of bounds on row.
            print('Try again.')
            continue
    break

#This is when you are choosing the row you are inputting.
while True:
    cole = False
    myShipLength = 2
    try:
        int(myShipLength)
    except:
        print("Try again.")
        cole = True
        continue
    if cole != True:
        if int(myShipLength) < 1 or int(myShipLength) >= 5: #This is checking for out of bounds on row.
            print('Try again.')
            continue
    break

#This is when you are choosing the row you are inputting.
while True:
    cole = False
    chooserR = input('Choose your Row: ')
    try:
        int(chooserR)
    except:
        print("Try again.")
        cole = True
        continue
    if cole != True:
        if int(myShipDir) == 0:
            if int(chooserR) < 1 or int(chooserR) > 10: #This is checking for out of bounds on row.
                print('Try again.')
                continue
        else:
            if int(chooserR) < 1 or int(chooserR) > 10+1-myShipLength: #This is checking for out of bounds on row.
                print('Try again.')
                continue
    break

#This is when you are choosing the column you are inputting.
while True:
    cole = False
    chooserC = input('Choose Your Col: ')
    try:
        int(chooserC)
    except:
        print("Try again.")
        cole = True
        continue
    if cole != True:
        if int(myShipDir) == 0:
            if int(chooserC) < 1 or int(chooserC) > 10+1-myShipLength: #This is checking for out of bounds on row.
                print('Try again.')
                continue
            else:
                if int(chooserC) < 1 or int(chooserC) > 10: #This is checking for out of bounds on row.
                    print('Try again.')
                    continue
    break
for i in range(myShipLength):
    if int(myShipDir) == 0:
        myarr[int(chooserC)+i-1][int(chooserR)-1] = "H"
    else:
        myarr[int(chooserC)-1][int(chooserR)+i-1] = "H"



#This method that will print the opponent board.
def printBoard(arr):
    print("Opponent: Chicago Bulls")
    for r in range(len(arr)):
        print(arr[r])
        print()
       

#This will print the user's board.       
def printMyBoard():
    print("Your Board: Lakers")
    for r in range(len(myarr)):
        print(myarr[r])
        print()
        




    

#This is storing the list of allMoves and allShips.
x = 0
row = random.randrange(0,int(arrSize))
col = random.randrange(0,int(arrSize))

allMoves = []
allShip = []



#This has something to do with the class of the ships.
allShip.append


#This will show you what round are you on.
while True:
    x += 1
    print("Round =", x)
    printBoard(myarr)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    printBoard(arr)


    #This is valadating the row input.
    while True:
        cole = False
        Trow = input('Choose Row: ')
        try:
            int(Trow)
        except:
            print("Try again.")
            cole = True
            continue
        if cole != True:
            if int(Trow) < 1 or int(Trow) > 10: #This is checking for out of bounds on row.
                print('Try again.')
                continue
        break

    #This is valadating the col input.
    while True:
        cole = False
        Tcol = input('Choose Col: ')
        try:
            int(Tcol)
        except:
            print("Try again.")
            cole = True
            continue
        if cole != True:
            if int(Tcol) < 1 or int(Tcol) > 10: #This is checking for out of bounds on row.
                print('Try again.')
                continue
        break

    #This defines the hold on the row and col.
    hold = Trow
    Trow = int(Tcol)-1
    Tcol = int(hold)-1

    holder = False
    allMoves.append(int(Trow))
    allMoves.append(int(Tcol))
    if arr[int(Trow)][int(Tcol)] == "X":
        print("Try again.")
        x-=1 #This is subtracting 1 from the round number.
    else:
        remover = 0
        for i in range(len(allShip)):
            if arr[int(Trow)][int(Tcol)] != "O" and arr[int(Trow)][int(Tcol)] != "X":
                print("You hit something at ", str(int(Tcol)+1) + " X, and at " + str(int(Trow)+1) + " Y")
                temp = arr[Trow][Tcol]
                arr[int(Trow)][int(Tcol)] = "X"
                count = 0
                for row in arr:
                    for i in row:
                        if i == temp:
                            count += 1
                if count == 0:
                    print("You destroyed the ship.")
                


#This code command is when you missed the target.
        if not holder:
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
        
    #This is checking the numbers of rounds left.
    if x >= 5:
        print("Eliminated.")
        quit()