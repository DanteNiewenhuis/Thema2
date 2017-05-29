import readMap
import dfs
import analyse
import sim_an_search

map = readMap.read_empty_map('NewChina.txt')

signal_cost = analyse.get_cost_scheme(4)
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
dfs.dfs(map, signals)
sim_an_search.sim_an(map, signal_cost, signals, begin_temp=10)

analyse.print_costs(map, signal_cost)
print(analyse.analyse_conflicts(map))
print(analyse.analyse_adjacent_states(map))
