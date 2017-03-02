import copy
import time

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

def find_empty(new_possible_list):
    minlength = 10
    place = [10, 10]
    for y in range(9):
        for x in range(9):
            if len(new_possible_list[y][x]) < minlength:
                minlength = len(new_possible_list[y][x])
                place = [y, x]
    if place == [10, 10]:
        return 0
    print(minlength)
    print(place)
    if minlength == 0:
        return 1
    return place

def processRij(x, num, mogelijkNum):
    for y in range(0,9):
        if num in mogelijkNum[x][y]:
            mogelijkNum[x][y].remove(num)
    return mogelijkNum

def processColumn(y, num, mogelijkNum):
    for x in range(0,9):
        if num in mogelijkNum[x][y]:
            mogelijkNum[x][y].remove(num)
    return mogelijkNum

def processBox(x, y, num, mogelijkNum):
    boxX = int(x/3)
    boxY = int(y/3)
    for x in range(3*boxX, 3*boxX + 3):
        for y in range(3*boxY, 3*boxY + 3):
            if num in mogelijkNum[x][y]:
                mogelijkNum[x][y].remove(num)
    return mogelijkNum

def process_number(place, number, new_possible_list):
    new_possible_list = processRij(place[1], number, new_possible_list)
    new_possible_list = processColumn(place[0], number, new_possible_list)
    new_possible_list = processBox(place[0], place[1], number, new_possible_list)
    return new_possible_list

def dfs(sudoku, possible_list):
    new_possible_list = copy.deepcopy(possible_list)
    print(new_possible_list)
    place = find_empty(new_possible_list)
    print(place)
    if place == 1:
        return False
    if place == 0:
        return True
    mogelijk_num = new_possible_list[place[0]][place[1]]
    new_possible_list[place[0]][place[1]] = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ]
    print(mogelijk_num)
    for number in mogelijk_num:
        new_possible_list = process_number(place, number, new_possible_list)
        for row in sudoku:
            print(row)
        print("")
        checker = dfs(sudoku, new_possible_list)
        if checker:
            return True
    if len(mogelijk_num) != 0:
        sudoku[place[0]][place[1]] = 0
    return False

def start_dfs(sudoku):
    possible_list = []
    for y in range(0,9):
        rij = []
        for x in range(0,9):
            if sudoku[y][x] == 0:
                rij.append([1,2,3,4,5,6,7,8,9])
            else:
                rij.append([sudoku[y][x]])
        possible_list.append(rij)
    return possible_list

start = time.time()
sudoku = readSudoku("puzzle3.sudoku")
possible_list = start_dfs(sudoku)
dfs(sudoku, possible_list)

for row in sudoku:
    print(row)
print("")
end = time.time()
print(end-start)