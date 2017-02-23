import random

def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]


def makeMutableList(sudoku):
    mList = []
    for y in range(0, 9):
        rij = []
        for x in range(0, 9):
            if (sudoku[y][x] == 0):
                rij.append(x)
        mList.append(rij)
    return mList


def makePossibleList(sudoku):
    pList = []
    for row in sudoku:
        posList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index in row:
            if index in posList:
                posList.remove(index)
        pList.append(posList)
    return pList


def fillSudoku():
    possableNumbers = makePossibleList(sudoku)
    for x in range(0, 9):
        posNumbers = possableNumbers[x]
        for y in range(0, 9):
            if sudoku[x][y] == 0:
                num = random.choice(posNumbers)
                posNumbers.remove(num)
                sudoku[x][y] = num

def swapNumbers(sudoku):
    row = random.randint(0,8)
    x1 = random.choice(isMutableList[row])
    x = random.choice(isMutableList[row])
    while x == x1:
        x = random.choice(isMutableList[row])
    x2 = x
    a = sudoku[row][x1]
    b = sudoku[row][x2]
    sudoku[row][x1] = b
    sudoku[row][x2] = a
    return sudoku

def checkColumn(x, oy, num, sudoku):
    numList = []
    for y in range(0, 9):
        if y != oy:
            numList.append(sudoku[y][x])
    if num in numList:
        return 1
    else:
        return 0

def findBox(ox, oy, boxX,boxY,sudoku):
    result = []
    for y in range (boxY*3,boxY*3+3):
        for x in range(boxX*3,boxX*3+3):
            if ox!= x:
                result.append(sudoku[y][x])
            elif oy!= y:
                result.append(sudoku[y][x])
    return result

def checkBox(x, y, num, sudoku):
    boxX = int(x / 3)
    boxY = int(y / 3)
    numList = findBox(x, y, boxX,boxY,sudoku)
    if num in numList:
        return 1
    else:
        return 0

def checkConflicts(sudoku):
    conflicts = 0
    for y in range(0,9):
        for x in range(0,9):
            num = sudoku[y][x]
            conflicts = conflicts + checkColumn(x, y,num,sudoku)
            conflicts = conflicts + checkBox(x, y , num,sudoku)
    return conflicts

sudoku = readSudoku("complete.sudoku")
isMutableList = makeMutableList(sudoku)
fillSudoku()
conflictCounter = checkConflicts(sudoku)
for row in sudoku:
    print(row)
print(conflictCounter)
for i in range(0,1000):
    newSudoku = swapNumbers(sudoku)
    newConflicts = checkConflicts(newSudoku)
    if newConflicts <= conflictCounter:
        conflictCounter = newConflicts
        sudoku = newSudoku
print("")
for row in sudoku:
    print(row)
print(conflictCounter)
