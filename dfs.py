def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

sudoku = readSudoku("puzzle1.sudoku")

def numbers_place()
##

def find_empty()
##zoek het (volgende) lege vakje in de sudoku
##optimalisatie idee: zoek het vakje met de minste opties en kies die als volgende
##return coordinaat

def put_number()


def dfs(sudoku)
        find_empty()
        number_place()
        for number in mogelijk_num
            put_number()
            dfs(sudoku)
            if succes()
                return True
        return False

