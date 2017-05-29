import readMap
import hill_solve
import statistics
import analyse

for x in range(1,26):
    map = readMap.read_complete_map('Russiadfs5.csv')
    signal_costs = analyse.get_cost_scheme(x)
    signal = ['zA', 'zB', 'zC', 'zD', 'zE']
    result = hill_solve.random_walker(map, signal_costs, signal)
    with open('stats_walker_5', 'a') as text:
        text.write(str(x))
        text.write(',')
        text.write(str(round(statistics.stdev(result))))
        text.write('\n')