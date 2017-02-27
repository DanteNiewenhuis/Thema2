def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

sudoku = readSudoku("puzzle1.sudoku")

def numbers_place()
##maak een lijst met mogelijke nummers voor het huidige coordinaat
##doe dit door te checken voor rij, kolom en box
##return deze lijst als mogelijk_num

def find_empty()
##zoek het (volgende) lege vakje in de sudoku
##optimalisatie idee: zoek het vakje met de minste opties en kies die als volgende
##return coordinaat

def put_number()


def dfs(sudoku)
        place = find_empty()
        mogelijk_num = number_place(place)
        for number in mogelijk_num
            put_number()
            dfs(sudoku)
            if succes()
                return True
        return False

