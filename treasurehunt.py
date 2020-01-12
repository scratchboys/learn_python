import random

PreviousLocation = []
TreasurePos = []
RANGEX = 60
RANGEY = 15
Board = []


# draw ocean area per Board
# ~~`~~~~~~```~~~~~~~~
# ~~`~~~~~~```~~~~~~~~
def drawMap(rows, columns) :
    for r in range (rows) :
        row_str = ''
        for c in range (columns) :
            row_str = row_str + Board[r][c]
        print(row_str)    



# '~' or '`` is used to present ocean location
# ocean has area of 15 (RANGEY) x 60 (RANGEX)
# ~~`~~~~~~```~~~~~~~~
# ~~`~~~~~~```~~~~~~~~
# store ocean map in Board

def oceanMap(rows, columns) :
    for r in range (rows) :
        Board.append([])
        for c in range (columns) :
            if random.randint(0, 1) :
                Board[r].append('~')
            else :
                Board[r].append('`')





# generate 3 random positions(x,y) of treasure
# in the specific area (RANGEX=60, RANGEY=15)
# output: [(x0,y0),(x1,y1),(x2,y2)]
#         3 positions must be different
def treasurePositions() :
    while len(TreasurePos) < 3:
        x = random.randint(0, RANGEX-1)
        y = random.randint(0, RANGEY-1)
        if (x, y) not in TreasurePos:
            TreasurePos.append((x, y))


#input option: 
#  1. quit
#  2. position (x, y)
def takePlayerInput() :
    while True :
        inp = input("Where to sonar device: ")
        (x, y) = (60, 15)
        if inp.lower() == "quit" :
            x = 99
            print("Ok quit. See you later")
            break
        else :    
            p = inp.split()
            if (len(p)==2 and p[0].isdigit() and p[1].isdigit()) :
                x = int(p[0])
                y = int(p[1])
                if (x>59 or y>14) :
                    print("the location is out of range")
                    continue
                elif (x,y) in PreviousLocation :
                    print("this location was picked")
                    continue
                else :
                    PreviousLocation.append((x,y))   
                    break
            else :
                print("Please input quit or valid location")
                continue    
    return (x, y)




def distance(p1, p2) :
    xdiff = (p1[0]-p2[0])
    ydiff = (p1[1]-p2[1])
    dd = xdiff*xdiff + ydiff*ydiff
    if (dd == 0)  :
        return 0
    elif dd == 1  :
        return 1
    elif dd <= 4   :
        return 2
    elif dd <= 9   :
        return 3
    elif dd <= 16 :
        return 4
    elif dd <= 25 :
        return 5
    elif dd <= 36 :
        return 6  
    elif dd <= 49 :
        return 7  
    elif dd <= 64 :
        return 8                       
    elif (dd <= 81) :
        return 9  
    else :
        return 10
