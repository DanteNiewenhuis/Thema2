import readMap
import dfs
import hill_solve
import draw
import sim_an_search
import analyse
import copy

for x in [1,2,3,4]:
    map = readMap.read_empty_map('New_Russia')
    signal_costs = analyse.get_cost_scheme(x)
    signals = list(signal_costs.keys())
    dfs.dfs(map, signals)
    sim_an_search.sim_an(map, signal_costs, signals, 2000, 5, 0.001)
    analyse.print_costs(map, signal_costs, print_before=str(x)+ ' = ')