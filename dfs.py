def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

def check_row(place, mogelijk_num, sudoku):
    y = place[0]
    for x in range (9):
        if sudoku[y][x] in mogelijk_num:
            mogelijk_num.remove(sudoku[y][x])
    return mogelijk_num

def check_col(place, mogelijk_num, sudoku):
    x = place[1]
    for y in range(9):
        if sudoku[y][x] in mogelijk_num:
            mogelijk_num.remove(sudoku[y][x])
    return mogelijk_num

def check_box(place, mogelijk_num, sudoku):
    boxX = int(place[1]/3)
    boxY = int(place[0]/3)
    for y in range(3*boxY, 3*boxY+3):
        for x in range(3*boxX, 3*boxX+3):
            if sudoku[y][x] in mogelijk_num:
                mogelijk_num.remove(sudoku[y][x])
    return mogelijk_num

def numbers_place(place, sudoku):
    mogelijk_num = [1,2,3,4,5,6,7,8,9]
    mogelijk_num = check_row(place, mogelijk_num, sudoku)
    mogelijk_num = check_col(place, mogelijk_num, sudoku)
    mogelijk_num = check_box(place, mogelijk_num, sudoku)
    return mogelijk_num


##maak een lijst met mogelijke nummers voor het huidige coordinaat
##doe dit door te checken voor rij, kolom en box
##return deze lijst als mogelijk_num

def find_empty(sudoku):
    ##zoek het (volgende) lege vakje in de sudoku
    ##check of sudoku succesvol vol is. if so: sudoku_success()
    ##optimalisatie idee: zoek het vakje met de minste opties en kies die als volgende
    for y in range (9):
        for x in range (9):
            if sudoku[y][x] == 0:
                return [y,x]
    return 0
        ##of zoiets, als alles vol is is de sudoku klaar
        ## nog even over nadenken

def dfs(sudoku):
        place = find_empty(sudoku)
        if place == 0:
            return True
        mogelijk_num = numbers_place(place, sudoku)
        for number in mogelijk_num:
            sudoku[place[0]][place[1]] = number
            checker = dfs(sudoku)
            if checker == True:
                return True
        if len(mogelijk_num) != 0:
            sudoku[place[0]][place[1]] = 0
        return False

sudoku = readSudoku("puzzle4.sudoku")
dfs(sudoku)
for row in sudoku:
    print(row)
#print(check_box([0,5], [1,2,3,4,5,6,7,8,9], sudoku))