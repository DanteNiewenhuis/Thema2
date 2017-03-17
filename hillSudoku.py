import random
import copy

# lees de sudoku in en maar er een multidimensional list van.
def readSudoku(name):
    with open(name, "r") as puzzle:
        return [[int(i) for i in line.split(",")] for line in puzzle]

# maak een multidimensional list waarin staat welke indexen mogen worden
# aangepast en welke niet.
def makeMutableList(sudoku):
    mList = []
    for y in range(0, 9):
        rij = []
        for x in range(0, 9):
            if (sudoku[y][x] == 0):
                rij.append(x)
        mList.append(rij)
    return mList

# maak een lijst van de mogelijke nummers die er in een rij kunnen
# worden gezet.
def makePossibleList(baseSudoku):
    pList = []
    for row in baseSudoku:
        posList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index in row:
            if index in posList:
                posList.remove(index)
        pList.append(posList)
    return pList

# vul alle rijen van de sudoku willekeurig met de getallen uit de Possiblelist.
# elk getal mag maar één keer in de rij voorkomen.
def fillSudoku(possableNumbers, baseSudoku):
    for x in range(0, 9):
        posNumbers = copy.deepcopy(possableNumbers[x])
        for y in range(0, 9):
            if baseSudoku[x][y] == 0:
                num = random.choice(posNumbers)
                posNumbers.remove(num)
                baseSudoku[x][y] = num

# kies een willekeurige rij en draai twee index die aangepast mogen worden
# met elkaar.
def swapNumbers(baseSudoku, isMutableList):
    sudoku = copy.deepcopy(baseSudoku)
    row = random.randint(0,8)
    x1 = random.choice(isMutableList[row])
    x = random.choice(isMutableList[row])
    while x == x1:
        x = random.choice(isMutableList[row])
    x2 = x
    a = sudoku[row][x1]
    sudoku[row][x1] = sudoku[row][x2]
    sudoku[row][x2] = a
    return sudoku

# controleer of er in de colom hetzelfde getal staat. Als dit zo is
# is er een conflict en wordt de conflict_counter een hoger
def checkColumn(x, num, sudoku):
    numList = []
    for y in range(0, 9):
        numList.append(sudoku[y][x])
    conflict_counter = 0
    for x in numList:
        if (num == x):
            conflict_counter = conflict_counter + 1
    return conflict_counter - 1

# vindt de box die bij de x en y hoort en return de waardes van alle
# indexen in deze box.
def findBox(ox, oy, sudoku):
    result = []
    boxX = int(ox / 3)
    boxY = int(oy / 3)
    for y in range (boxY*3, boxY*3 + 3):
        for x in range(boxX*3, boxX*3 + 3):
            result.append(sudoku[y][x])
    return result

# controleer of de index en conflict in zijn box heeft.
def checkBox(x, y, num, sudoku):
    numList = findBox(x, y, sudoku)
    counter = 0
    for x in numList:
        if (num == x):
            counter = counter + 1
    return counter - 1

# controleer hoeveel conflicten er zijn in de gegeven sudoku.
def checkConflicts(sudoku):
    conflicts = 0
    for y in range(0,9):
        for x in range(0,9):
            num = sudoku[y][x]
            conflicts = conflicts + checkColumn(x, num, sudoku)
            conflicts = conflicts + checkBox(x, y , num, sudoku)
    return conflicts


def run_hillclimber(puzzle):
    # lees de sudoku, vindt de indexen die geweizigd mogen worden en vul de sukdoku met
    # willekeurige getallen
    baseSudoku = readSudoku(puzzle)
    isMutableList = makeMutableList(baseSudoku)
    possableNumbers = makePossibleList(baseSudoku)
    fillSudoku(possableNumbers, baseSudoku)
    conflictCounter = checkConflicts(baseSudoku)
    currentConflicts = conflictCounter
    counter = 0

    # verwissel de waardes van twee indexen van een willekeurige rij.
    # behoudt de nieuwe sudoku als deze wisseling voor minder of even veel conflicten zorgt.
    # ga verder met de oude sudoku als er meer conflicten zijn.
    while(conflictCounter != 0):

        # bekijk elke 200 iteraties hoeveel conflicten er zijn. als dit na 200 iteraties niet veranderd
        # is wordt de sudoku opnieuw met willekeurige getallen gevult.
        if(counter % 200 == 0):
            if currentConflicts == conflictCounter:
                baseSudoku = readSudoku(puzzle)
                isMutableList = makeMutableList(baseSudoku)
                possableNumbers = makePossibleList(baseSudoku)
                fillSudoku(possableNumbers, baseSudoku)
                conflictCounter = checkConflicts(baseSudoku)
                currentConflicts = conflictCounter
            else:
                currentConflicts = conflictCounter
        newSudoku = swapNumbers(baseSudoku, isMutableList)
        newConflicts = checkConflicts(newSudoku)

        if (newConflicts <= conflictCounter):
            conflictCounter = newConflicts
            baseSudoku = copy.deepcopy(newSudoku)
        counter += 1
    for row in baseSudoku:
        print(row)

run_hillclimber("puzzle3.sudoku")