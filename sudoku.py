puzzle = open("puzzle1.sudoku", "r")

def checkRow(list,







sudoku = []
for line in puzzle:
    rij = line.split(",")
    sudoku.append(rij)
