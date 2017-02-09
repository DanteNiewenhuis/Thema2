puzzle = open("puzzle1.sudoku", "r")

def checkRow(y):
    row = sudoku[y]
    result = [1,2,3,4,5,6,7,8,9]
    for q in row:
        if int(q) in result:
            result.remove(int(q))
    return result

def makeColumn(x):
    column = []
    for q in range(x, len(sudoku), 9):
        column.append(sudoku[q])
    return column

def checkColumn(x,pNum):
    column = makeColumn(x)
    for q in column:
        if int(q) in pNum:
            pNum.remove(int(q))
    return pNum

sudoku = []
for line in puzzle:
    rij = line.split(",")
    for coord in rij:
        sudoku.append(coord)

print(makeColumn(0))


#for y in range(0,9):
#    for x in range(0,9):
#        if (sudoku[y][x]):
#            pNum = checkRow(y)
#            pNum = checkColumn(x,pNum)
#            pNum = checkBox(x,y,pNum)
#            if(pNum.length == 1):
#                sudoku[y][x] = pNum[0]

