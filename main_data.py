import hillSudoku
import read_data

for amount in [100,200,300,400,500,750,1000]:
    list = hillSudoku.test(amount)
    read_data.convert(amount, list)