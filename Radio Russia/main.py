import readMap
import dfs
import analyse
import hill_solve

map = readMap.readStates("UnitedStates.txt")
print(analyse.analyse_adjacent_states(map))
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
dfs.dfs(map, signals)
#for state in map:
#    print(str(state) + ' = ' + str(state.signal))

print("analyse: ")
print(analyse.analyse_conflicts(map))
freq = analyse.signal_frequentie(map)
list_freq = freq.keys()
for signal in sorted(list_freq):
    print(signal, freq[signal])

print(analyse.get_cost(freq, costs))
hill_solve.hill_climber(map, costs, signals)
freq = analyse.signal_frequentie(map)
list_freq = freq.keys()
for signal in sorted(list_freq):
    print(signal, freq[signal])
print(analyse.get_cost(freq, costs))