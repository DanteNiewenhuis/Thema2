import random
import copy

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
    for row in baseSudoku:
        posList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index in row:
            if index in posList:
                posList.remove(index)
        pList.append(posList)
    return pList

def fillSudoku(possableNumbers):
    for x in range(0, 9):
        posNumbers = copy.deepcopy(possableNumbers[x])
        for y in range(0, 9):
            if baseSudoku[x][y] == 0:
                num = random.choice(posNumbers)
                posNumbers.remove(num)
                baseSudoku[x][y] = num

def swapNumbers(baseSudoku):
    sudoku = copy.deepcopy(baseSudoku)
    row = random.randint(0,8)
    x1 = random.choice(isMutableList[row])
    x = random.choice(isMutableList[row])
    while x == x1:
        x = random.choice(isMutableList[row])
    x2 = x
    a = sudoku[row][x1]
    sudoku[row][x1] = sudoku[row][x2]
    sudoku[row][x2] = a
    return sudoku

def checkColumn(x, oy, num, sudoku):
    numList = []
    for y in range(0, 9):
        numList.append(sudoku[y][x])
    counter = 0
    for x in numList:
        if (num == x):
            counter = counter + 1
    return counter - 1

def findBox(ox, oy, sudoku):
    result = []
    boxX = int(ox / 3)
    boxY = int(oy / 3)
    for y in range (boxY*3, boxY*3 + 3):
        for x in range(boxX*3, boxX*3 + 3):
            result.append(sudoku[y][x])
    return result

def checkBox(x, y, num, sudoku):
    numList = findBox(x, y, sudoku)
    counter = 0
    for x in numList:
        if (num == x):
            counter = counter + 1
    return counter - 1

def checkConflicts(sudoku):
    conflicts = 0
    for y in range(0,9):
        for x in range(0,9):
            num = sudoku[y][x]
            conflicts = conflicts + checkColumn(x, y, num, sudoku)
            conflicts = conflicts + checkBox(x, y , num, sudoku)
    return conflicts

baseSudoku = readSudoku("puzzle3.sudoku")
isMutableList = makeMutableList(baseSudoku)
possableNumbers = makePossibleList(baseSudoku)
fillSudoku(possableNumbers)
#baseSudoku = readSudoku("complete.sudoku")
conflictCounter = checkConflicts(baseSudoku)
counter = 0
print(conflictCounter)
for row in baseSudoku:
    print(row)
backupCounter = 0
while (conflictCounter != 0):
    counter = counter + 1
    if(counter % 500 == 0):
        print(conflictCounter)
        if(conflictCounter == 8 or conflictCounter == 4):
            for row in baseSudoku:
                print(row)
    #if(counter % 2000 == 0):
    #    print(conflictCounter)
    #    baseSudoku = readSudoku("puzzle3.sudoku")
    #    fillSudoku(possableNumbers)
    #    conflictCounter = checkConflicts(baseSudoku)
    newSudoku = copy.deepcopy(baseSudoku)
    newSudoku = swapNumbers(baseSudoku)
    newConflicts = checkConflicts(newSudoku)
    if (newConflicts <= conflictCounter or backupCounter == 200):
        conflictCounter = newConflicts
        baseSudoku = copy.deepcopy(newSudoku)
        backupCounter = 0
    else:
        backupCounter = backupCounter + 1
for row in baseSudoku:
    print(row)
print(conflictCounter)
print(counter)