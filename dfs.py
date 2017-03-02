
def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

#check_ row, col, box, all work in a similar way.
#They check what numbers are still possible for a given x,y coordinate
#in the sudoku. They check what numbers are already
#in the row/column/box, and remove that number from a 1 to 9 list.
#that list is returned as mogelijk_num.
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

#the two successive for loops define the box of a sudoku,
#by moving down a line after three steps to the right.
def check_box(place, mogelijk_num, sudoku):
    boxX = int(place[1]/3)
    boxY = int(place[0]/3)
    for y in range(3*boxY, 3*boxY+3):
        for x in range(3*boxX, 3*boxX+3):
            if sudoku[y][x] in mogelijk_num:
                mogelijk_num.remove(sudoku[y][x])
    return mogelijk_num

#combine check row/column/box to a list that contains
#the possible numbers for a x,y coordinate in the sudoku
def numbers_place(place, sudoku):
    mogelijk_num = [1,2,3,4,5,6,7,8,9]
    mogelijk_num = check_row(place, mogelijk_num, sudoku)
    mogelijk_num = check_col(place, mogelijk_num, sudoku)
    mogelijk_num = check_box(place, mogelijk_num, sudoku)
    return mogelijk_num

#go over sudoku from left to right, line by line,
#to find a place where the number is zero
#pick that place and return x,y coordinate
#if there are no 0's left in the sudoku, return 0 and end process
def find_empty(sudoku):
    for y in range (9):
        for x in range (9):
            if sudoku[y][x] == 0:
                return [y,x]
    return 0

# this is the piece that does all the work of solving the sudoku
# start with first empty place, fill in first possible value,
# continue to next empty space, repeat.
# this process continues until it's not possible to fill in a value on an empty spot
# backtrack to last filled in value, change it to the next possible value for that spot
# then try again.
# repeat this process until sudoku is solved
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

#choose sudoku file
sudoku = readSudoku("puzzle4.sudoku")
import time
#start = time.time()

#run depth first search
dfs(sudoku)
#end = time.time()
#print(end-start)

#print sudoku
for row in sudoku:
    print(row)