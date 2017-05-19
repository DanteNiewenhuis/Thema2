import readMap
import dfs
import analyse
import hill_solve
import sim_an_search
import draw

l = []
with open('China.txt', 'r') as text:
    for line in text:
        line = line.strip('\n')
        split_line = line.split(',')
        l.append(split_line)
with open('New_China', 'w') as text:
    for line in l:
        text.write(line[0])
        text.write(',')
        for word in line:
            text.write(word)
            text.write(',')
        text.write('\n')