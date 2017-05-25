import analyse
import readMap
import sim_an_search
import hill_solve
import statistics

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
count = 1

with open("randomwalk.txt", 'r') as text:
    with open("walkstats.txt", 'w') as text2:
        for line in text:
            text2.write(str(count) + ', ')
            list = []
            split_line = line.split(',')
            for x in split_line:
                if x is not '\n':
                    list.append(int(x))
            avg = sum(list)/float(len(list))
            std = statistics.stdev(list)
            text2.write(str(avg) + ', ')
            text2.write(str(std) + ', ')
            text2.write('\n')
            count += 1



