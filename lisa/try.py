def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

def processRij(x, num):
    for y in range(0,9):
        if num in mogelijkNum[x][y]:
            mogelijkNum[x][y].remove(num)

def processColumn(y, num):
    for x in range(0,9):
        if num in mogelijkNum[x][y]:
            mogelijkNum[x][y].remove(num)

def processBox(x, y, num):
    boxX = int(x/3)
    boxY = int(y/3)
    for x in range(3*boxX, 3*boxX + 3):
        for y in range(3*boxY, 3*boxY + 3):
            if num in mogelijkNum[x][y]:
                mogelijkNum[x][y].remove(num)

def checkMogelijkeNum(sudoku):
    mogelijkNum = []
    for line in sudoku:
        rij = []
        for num in line:
            if(num == 0):
                rij.append([1,2,3,4,5,6,7,8,9])
            else:
                rij.append([num])
        mogelijkNum.append(rij)
    return mogelijkNum

def isSudokuNotFull():
    for x in range(0,9):
        for y in range(0,9):
            if sudoku[x][y] == 0:
                return True
    return False


sudoku = readSudoku("puzzle1.sudoku")

mogelijkNum = checkMogelijkeNum(sudoku)

while(isSudokuNotFull()):
    for x in range(0,9):
        for y in range(0,9):
            if len(mogelijkNum[x][y])== 1:
                    value = mogelijkNum[x][y][0]
                    print(value, "is value")
                    sudoku[x][y] = value
                    processRij(x, value)
                    processColumn(y, value)
                    processBox(x, y, value)

for line in sudoku:
    print(line)


