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

sudoku = readSudoku("puzzle1.sudoku")
mogelijkNum = checkMogelijkeNum(sudoku)

for x in range(0,9):
    for y in range(0,9):
        if len(mogelijkNum[x][y])== 1:
            q = mogelijkNum[x][y][0]
            mogelijkNum[x][y][0] = "x"
            sudoku[x][y] = q
            processRij(x, q)
print(mogelijkNum)