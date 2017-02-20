def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

sudoku = readSudoku("puzzle1.sudoku")

print(sudoku)

