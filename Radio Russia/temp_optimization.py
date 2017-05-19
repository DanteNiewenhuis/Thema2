import analyse
import readMap
import random

begin_temp = 0
end_temp = 0
best_score = 0
average_score = 0
with open('best_temp_4.txt', 'r') as text:
    for line in text:
        split_line = line.split(',')
        begin_temp = int(split_line[0])
        end_temp = int(split_line[1])
        best_score = int(split_line[2])
        average_score = int(split_line[3])

while(True):
    begin_temp += random.choice([-3, -2, -1, 0, 1, 2, 3])
    end_temp += random.choice([-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3])
    for x in range(10):
        

