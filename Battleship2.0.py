import random
#Made by Don
while True:
    cole = False
    arrSize = input('Choose How big you want your Ocean: ')
    try: 
        int(arrSize)
    except:
        print("Please provide an single number")
        cole = True
        continue
    if cole != True:
        if int(arrSize) < 3: 
            print('Come on now damn it')
            continue
    break
    
arr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]
myarr = [["O" for i in range(int(arrSize))] for i in range(int(arrSize))]


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
        if int(chooserR) < 0 or int(chooserR) >= int(arrSize): #checking for out of bounds on row
            print('Yeahhh i think you slow ben hawk')
            continue
    break

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
        if int(chooserC) < 0 or int(chooserC) >= int(arrSize): #checking for out of bounds on row
            print('OH MY COME ONNNN!!!')
            continue
    break
myarr[int(chooserR)][int(chooserC)] = "H"


#method that will print the bord
def printBoard():
    print("The Oppositions")
    for r in range(len(arr)):
        print(arr[r])
        print()
        
def printMyBoard():
    print("Your Board")
    for r in range(len(myarr)):
        print(myarr[r])
        print()

class ship():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name


x = 0
row = random.randrange(0,int(arrSize))
col = random.randrange(0,int(arrSize))
print(str(col) + " , " + str(row))
allMoves = []
allShip = []

ship1 = ship(row,col,"Lefter")
allShip.append(ship1)

while True:
    x += 1
    print("Round =", x)
    printBoard()

    #valadating the row input
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
            if int(Trow) < 0 or int(Trow) > 4: #checking for out of bounds on row
                print('Please enter a number in the bounds.')
                continue
        break

    #valadating the col input
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
            if int(Tcol) < 0 or int(Tcol) > 4: #checking for out of bounds on row
                print('enter a number in the bounds.')
                continue
        break

    #idk man
    hold = Trow
    Trow = Tcol
    Tcol = hold

    holder = False
    allMoves.append(int(Trow))
    allMoves.append(int(Tcol))
    if arr[int(Trow)][int(Tcol)] == "X":
        print("you have already did that Stooopiddd")
        x-=1 # subtract 1 from the round number
    else:
        remover = 0
        for i in range(len(allShip)):
            if int(allShip[i].x) == int(Trow) and int(allShip[i].y) == int(Tcol):
                print("You Hit Something at ", Tcol + " X, and at " + Trow + " Y")
                arr[int(Trow)][int(Tcol)] = "X"
                print("Ship Was Destoryed, You Win")
                quit()

        if not holder:
            print("Miss!")
            arr[int(Trow)][int(Tcol)] = "X"
    attackR = random.randrange(0,int(arrSize))
    attackC = random.randrange(0,int(arrSize))
    while myarr[attackR][attackC] == "X":
        attackR = random.randrange(0,int(arrSize))
        attackC = random.randrange(0,int(arrSize))
    if myarr[attackR][attackC] == "H":
        myarr[attackR][attackC] = 'X'
        printMyBoard()
        print('You died bum')
        quit()
    else:
        myarr[attackR][attackC] = 'X'
        printMyBoard()
        
    #if round is 5 or greater than 5 then the game is over and you lost.. loser
    if x >= 5:
        print("You have been eliminated hahahaha")
        quit()