import readMap
import analyse
import dfs
import hill_solve

map = readMap.read_empty_map('Russia.txt')

signals = ['zA', 'zB', 'zC', 'zD']
dfs.dfs(map, signals)

with open('Russiadfs4.csv', 'w') as text:
    for state in map:
        text.write(str(state.name))
        text.write(',')
        text.write(str(state.code))
        text.write(',')
        text.write(str(state.signal))
        text.write(',')
        for adj in state.adjacent_states:
            text.write(str(adj))
            text.write(',')
        text.write('\n')