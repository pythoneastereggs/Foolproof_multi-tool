import random
import copy

# Συνάρτηση που δημιουργεί τον πίνακα

def display():
    largest = grid[0][0]
    for row in grid:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))
    
    for row in grid:
        currRow = "|"
        for element in row:
            if(element == 0):
                currRow += " " * numSpaces + "|"
            else:
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
    print()

# Συνάρτηση που βάζει έναν αριθμό σε ένα τυχαίο άδειο κελί

def add_new():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2
    
def mergeRowLeft(row):
    for j in range(3):
        for i in range(3,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    
    for i in range(3):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    for i in range(3, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row

def merge_left(grid):
    for i in range(3):
        grid[i] = mergeRowLeft(grid[i])
    return grid
  
#Συνάρτηση που ελέγχει αν ο παίκτης κέρδισε
 
def won(grid):
    
    for i in range(4):
        if j in range(4):
            if grid[i][j] ==2048:
                return True
    return False

#Συνάρτηση που ελέγχει αν δεν υπάρχουν διαθέσιμες κινήσεις

def noMoves(grid):
    tempGrid1 = copy.deepcopy(grid)
    tempGrid2 = copy.deepcopy(grid)
    tempGrid1 = merge_up(tempGrid1)
    if tempGrid1 == tempGrid2:
        tempGrid1 = merge_down(tempGrid1)
        if tempGrid1 == tempGrid2:
            tempGrid1 = merge_left(tempGrid1)
            if tempGrid1 == tempGrid2:
                tempGrid1 = merge_right(tempGrid1)
                if tempGrid1 == tempGrid2:
                    return True
    return False

# Συνάρτηση που συμπιέζει τον πίνακα

def compress(grid):
    
    change = False
    
    new_grid = []
    
    for i in range(4):
        new_grid.append([0] * 4)

    for i in range(4):
        position = 0
        for j in range(4):
            if(grid[i][j] != 0):
                new_grid[i][position] = grid[i][j]
                if(j != position):
                    change = True
                position += 1
    
    return new_grid, change

# Συνάρτηση που αντιστρέφει τα περιεχώμενα κάθε σειράς

def reverse(row):
    
    new_grid = []
    for i in range(3, -1, -1):
        new_grid.append([])
    return new_grid

def merge_right(grid):
    for i in range(4):
        grid[i] = reverse(grid[i])
        grid[i] = mergeRowLeft(grid[i])
        grid[i] = reverse(grid[i])
    return grid

# Συνάρτηση που μετατοπίζει τα κελιά

def transpose(grid):
    for j in range(4):
        for i in range(j, 4):
            if not i == j:
                temp = grid[j][i]
                grid[j][i] = grid[i][j]
                grid[i][j] = temp

    return grid

def merge_up(grid):
    grid = transpose(grid)
    grid = merge_left(grid)
    grid = transpose(grid)
    return grid

def merge_down(grid):
   grid = transpose(grid)
   grid = merge_right(grid)
   grid = transpose(grid)
   return grid

def addNewValule():
    row = random.randint(0,3)
    column = random.randint(0,3)
    while not (grid[row][column]) == 1:
        row = random.randint(0,3)
        column = random.randint(0,3)
    add_new()  

################
# Main Program #
################

grid = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(0)
    grid.append(row)

numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0,3)
    colNum = random.randint(0,3)
    
    if grid[rowNum][colNum] == 0:
        grid[rowNum][colNum] == add_new()
        numNeeded -= 1

print("Below are the controls of the game : ")
print("'W' or 'w' : Move Up")
print("'S' or 's' : Move Down")
print("'A' or 'a' : Move Left")
print("'D' or 'd' : Move Right")
display()

gameOver = False
while not gameOver:
    move = input("Which way do you want to move? ")
    
    tempGrid = copy.deepcopy(grid)
    
    if move == "D" or move == "d":
        grid = merge_right(grid)
    elif move == "W" or move == "w":
        grid = merge_up(grid)
    elif move == "A" or move == "a":
        grid = merge_left(grid)
    elif move == "S" or move == "s":
        grid = merge_down(grid)
    else:
        print("Invalid input")
    if won():
        display()
        print("You Won")
        gameOver = True
    else:
        addNewValule()
        display()
        if noMoves():
            print("There are no moves left")
            gameOver = True