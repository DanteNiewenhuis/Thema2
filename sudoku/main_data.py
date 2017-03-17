import time

from sudoku import hillSudoku

#for amount in [100,200,300,400,500,750,1000]:
#    list = hillSudoku.test(amount)
#    read_data.convert(amount, list)

start = time.time()
hillSudoku.run_hillclimber()
end = time.time()
elapsed = end - start
print(elapsed)
