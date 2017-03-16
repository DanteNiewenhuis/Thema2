import readMap
import dfs
import analyse

map = readMap.readStates("Oekraine.txt")
signals = ['zA', 'zB', 'zC', 'zD']
dfs.dfs(map, signals)

for state in map:
    print(state)
    print(state.adjacent_states)
    print(state.signal)