import analyse
import readMap
import dfs

map = readMap.read_empty_map('NewChina.txt')
signal_costs = analyse.get_cost_scheme(4)
signals = list(signal_costs.keys())
dfs.dfs(map, signals)
analyse.print_costs(map, signal_costs)

with open('Chinadfs.txt', 'w') as text:
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
