import analyse
import readMap
import random
import sim_an_search

s = '3'
begin_temp = 0
new_begin_temp = 0
end_temp = 0
new_end_temp = 0
best_score = 0
average_score = 0

c = analyse.get_cost_scheme(int(s))
signals = list(c.keys())

while(True):
    with open('best_temp_' + s + '.txt', 'r') as text:
        for line in text:
            split_line = line.split(',')
            begin_temp = int(split_line[0])
            end_temp = float(split_line[1])
            best_score = int(split_line[2])
            average_score = float(split_line[3])
            iterations = int(split_line[4])

    new_begin_temp = begin_temp + random.choice([-2, -1, 0, 1, 2])
    if new_begin_temp < 0:
        new_begin_temp = 1
    new_end_temp = end_temp + random.choice([-0.2, -0.1, 0, 0.1, 0.2])
    if new_end_temp < 0:
        new_end_temp = 0.1
    m = 0
    lowest_costs = 10000
    print('begin = ' + str(new_begin_temp) + ' end = ' + str(new_end_temp))
    for y in range(10):
        map = readMap.read_complete_map('Russiadfs.txt')
        map = sim_an_search.sim_an(map, c, signals, 200000, new_begin_temp, new_end_temp)
        freq = analyse.analyse_signal_frequentie(map)
        costs = analyse.get_cost(freq, c)
        if costs < lowest_costs:
            lowest_costs = costs
        m += costs
        print(y)
    mean = m / 10
    print('mean = '+str(mean)+' lowest = '+str(lowest_costs))
    iterations += 1
    if lowest_costs < best_score:
        with open('best_temp_'+ s +'.txt', 'w') as text:
            text.write(str(new_begin_temp))
            text.write(',')
            text.write(str(new_end_temp))
            text.write(',')
            text.write(str(lowest_costs))
            text.write(',')
            text.write(str(mean))
            text.write(',')
            text.write(str(iterations))
            text.write(',')

    elif lowest_costs == best_score:
        if mean < average_score:
            with open('best_temp_' + s + '.txt', 'w') as text:
                text.write(str(new_begin_temp))
                text.write(',')
                text.write(str(new_end_temp))
                text.write(',')
                text.write(str(lowest_costs))
                text.write(',')
                text.write(str(mean))
                text.write(',')
                text.write(str(iterations))
                text.write(',')
    if lowest_costs > best_score:
        with open('best_temp_' + s + '.txt', 'w') as text:
            text.write(str(begin_temp))
            text.write(',')
            text.write(str(end_temp))
            text.write(',')
            text.write(str(best_score))
            text.write(',')
            text.write(str(average_score))
            text.write(',')
            text.write(str(iterations))
            text.write(',')