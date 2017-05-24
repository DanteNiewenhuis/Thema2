import analyse
import readMap
import hill_solve


for x in range(1, 5):
    signal_costs = analyse.get_cost_scheme(int(x))
    signals = list(signal_costs.keys())
    costs_list = []
    for y in range(20):
        map = readMap.read_complete_map('Russiadfs.txt')
        hill_solve.hill_climber(map, signal_costs, signals, iterations=200000)
        freq = analyse.analyse_signal_frequentie(map)
        costs = analyse.get_cost(freq, signal_costs)
        costs_list.append(costs)
        print(costs)
    print('number = '+ str(x))
    with open('costs_stats_hill.txt', 'a') as text:
        text.write(str(x))
        text.write(',')
        for cost in costs_list:
            text.write(str(cost))
            text.write(',')
        text.write('\n')
