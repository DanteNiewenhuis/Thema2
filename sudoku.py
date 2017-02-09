puzzle = open("puzzle1.sudoku", "r")

def makeRow(num):
    row = []
    begin = y*9
    for q in range (begin,begin+9):
        row.append(sudoku[q])
    return row

def makeColumn(num):
    column = []
    for q in range(x, len(sudoku), 9):
        column.append(sudoku[q])
    return column

def checkRow(y):
    row = makeRow(y)
    result = [1,2,3,4,5,6,7,8,9]
    for q in row:
        if int(q) in result:
            result.remove(int(q))
    return result

def checkColumn(x,pNum):
    column = makeColumn(x)
    for q in column:
        if int(q) in pNum:
            pNum.remove(int(q))
    return pNum

def checkBox():


sudoku = []
for line in puzzle:
    rij = line.split(",")
    for coord in rij:
        sudoku.append(coord.strip("\n"))

x = checkRow(5)
print(checkColumn(5,x))



#for y in range(0,9):
#    for x in range(0,9):
#        if (sudoku[y][x]):
#            pNum = checkRow(y)
#            pNum = checkColumn(x,pNum)
#            pNum = checkBox(x,y,pNum)
#            if(pNum.length == 1):
#                sudoku[y][x] = pNum[0]

