import analyse
import readMap
import sim_an_search

<<<<<<< HEAD
for s in ['27']:
=======
for s in ['26']:
>>>>>>> origin/master
    signal_costs = analyse.get_cost_scheme(int(s))
    signals = list(signal_costs.keys())

    print('s = ' + s)
    for x in range(1, 31):
        print('temperature = ' + str(x))
        costs_list = []
        for y in range(20):
            map = readMap.read_complete_map('Russiadfs.txt')
            sim_an_search.sim_an(map, signal_costs, signals, begin_temp=x, end_temp=0.5)
            freq = analyse.analyse_signal_frequentie(map)
            costs = analyse.get_cost(freq, signal_costs)
            costs_list.append(costs)
            print(costs)
        with open('costs_stats_scheme' + s, 'a') as text:
            text.write(str(x))
            text.write(',')
            for cost in costs_list:
                text.write(str(cost))
                text.write(',')
            text.write('\n')
