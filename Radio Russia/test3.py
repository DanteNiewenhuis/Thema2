import readMap
import draw
import analyse
import dfs
import hill_solve

map = readMap.read_complete_map('best_map_america_2.txt')

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
hill_solve.hill_climber(map, signal_costs, signals)
freq = analyse.signal_frequentie(map)
for signal in freq:
    print(str(signal) + ' = ' + str(freq[signal]))
old_costs = analyse.get_cost(freq, signal_costs)
print(old_costs)