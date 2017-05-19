import analyse
import readMap
import random
import sim_an_search

s = '4'
begin_temp = 0
end_temp = 0
best_score = 0
average_score = 0

c = analyse.get_cost_scheme(int(s))
signals = list(c.keys())

while(True):
    with open('best_temp_' + s + '.txt', 'r') as text:
        for line in text:
            split_line = line.split(',')
            print(split_line)
            begin_temp = int(split_line[0])
            end_temp = float(split_line[1])
            best_score = int(split_line[2])
            average_score = float(split_line[3])

    begin_temp += random.choice([-3, -2, -1, 0, 1, 2, 3])
    if begin_temp < 0:
        begin_temp = 1
    end_temp += random.choice([-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3])
    if end_temp < 0:
        end_temp = 0.1
    m = 0
    lowest_costs = 10000
    print('begin = ' + str(begin_temp) + ' end = ' + str(end_temp))
    for y in range(10):
        map = readMap.read_complete_map('Russiadfs.txt')
        map = sim_an_search.sim_an(map, c, signals, 200000, begin_temp, end_temp)
        freq = analyse.analyse_signal_frequentie(map)
        costs = analyse.get_cost(freq, c)
        if costs < lowest_costs:
            lowest_costs = costs
        m += costs
        print(m)
    mean = m / 10
    print('mean = '+str(mean)+' lowest = '+str(lowest_costs))
    if lowest_costs < best_score:
        with open('best_temp_'+ s +'.txt', 'w') as text:
            text.write(str(begin_temp))
            text.write(',')
            text.write(str(end_temp))
            text.write(',')
            text.write(str(lowest_costs))
            text.write(',')
            text.write(str(mean))
            text.write(',')
    elif lowest_costs == best_score:
        if mean < average_score:
            with open('best_temp_' + s + '.txt', 'w') as text:
                text.write(str(begin_temp))
                text.write(',')
                text.write(str(end_temp))
                text.write(',')
                text.write(str(lowest_costs))
                text.write(',')
                text.write(str(mean))
                text.write(',')
    print('hoi')

