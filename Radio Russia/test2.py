import readMap
import dfs
import hill_solve
import analyse
import matplotlib.pyplot as plt

result = []
for x in range(1000):
    map = readMap.readStates('UnitedStates.txt')

    signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
    signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}

    dfs.dfs(map, signals)
    hill_solve.hill_climber(map, signal_costs, signals)
    new_freq = analyse.signal_frequentie(map)
    new_costs = analyse.get_cost(new_freq, signal_costs)
    result.append(new_costs)

dict = {}
for cost in result:
    if cost in dict:
        x = dict[cost]
        dict[cost] = x + 1
    else:
        dict[cost] = 1

sorted_keys = sorted(dict.keys())
sorted_dict = {}
for key in sorted_keys:
    sorted_dict[key] = dict[key]

print(sorted_dict)
plt.bar(range(len(sorted_dict)), sorted_dict.values(), align='center')
plt.xticks(range(len(sorted_dict)), sorted_dict.keys(), rotation='vertical')

plt.show()