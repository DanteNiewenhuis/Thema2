import readMap
import dfs
import analyse

map = readMap.readStates("Oekraine.txt")
print(analyse.analyse_adjacent_states(map))
signals = ['zA', 'zB', 'zC', 'zD']
dfs.dfs(map, signals)
for state in map:
    print(str(state) + ' = ' + state.signal)

print("analyse: ")
print(analyse.analyse_conflicts(map))
x = analyse.signal_frequentie(map)
list_x = x.keys()
for signal in sorted(list_x):
    print(signal, x[signal])