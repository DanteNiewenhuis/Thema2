def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

sudoku = readSudoku("puzzle1.sudoku")

def numbers_place(place)
    for iets
        check_row(place)
        check_col(place)
        check_box(place)
    return mogelijk_num


##maak een lijst met mogelijke nummers voor het huidige coordinaat
##doe dit door te checken voor rij, kolom en box
##return deze lijst als mogelijk_num

def find_empty(sudoku)
    ##zoek het (volgende) lege vakje in de sudoku
    ##check of sudoku succesvol vol is. if so: sudoku_success()
    ##optimalisatie idee: zoek het vakje met de minste opties en kies die als volgende
    for y in range 8
        for x in range 8
            if sudoku[y][x] == 0
                return [y,x]
    sudoku_success()
        ##of zoiets, als alles vol is is de sudoku klaar
        ## nog even over nadenken



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

