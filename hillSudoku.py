import random

def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

def makeMutableList(sudoku):
    mList = []
    for y in range(0,9):
        mList.append([True for x in range(0,9)])
    for y in range(0,9):
        for x in range(0,9):
            if (sudoku[y][x] != 0):
                mList[y][x] = False
    return mList

def makePossibleList(sudoku):
    pList = []
    for row in sudoku:
        posList = [1,2,3,4,5,6,7,8,9]
        for index in row:
            if index in posList:
                posList.remove(index)
        pList.append(posList)
    return pList

def fillSudoku():
    for x in range(0,9):
        posNumbers = possableNumbers[x]
        for y in range(0,9):
            if sudoku[x][y] == 0:
                num = random.choice(posNumbers)
                posNumbers.remove(num)
                sudoku[x][y] = num
def checkIndex(x,y,num):
    mogelijkeNummers = checkColumn(x)
    mogelijkeNummers = checkBox(x,y,mogelijkeNummers)


def checkColumn(x):
    result = [1,2,3,4,5,6,7,8,9]
    for y in range(0,9):
        if sudoku[y][x] in result:
            result.remove(sudoku[x][y])
    return result

def checkBox(x,y, mogelijkeNummers):
    boxX = x/3
    boxY = y/3
    return result

sudoku = readSudoku("puzzle1.sudoku")
isMutableList = makeMutableList(sudoku)
possableNumbers = makePossibleList(sudoku)
for row in sudoku:
    print(row)
fillSudoku()
#for rij in isMutableList:
#    print(rij)
print("")
for row in sudoku:
    print(row)

print(checkColumn(2))