import readMap
import analyse

map = readMap.readStates('UnitedStates.txt')
signals = ['zA', 'zB', 'zC', 'zD']
dfs.dfs(map, signals)
print(analyse.analyse_adjacent_states(map))