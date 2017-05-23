import analyse
import sim_an_search
import readMap
import hill_solve
import dfs


map = readMap.read_complete_map('Russiadfs.txt')

signal_costs = analyse.get_cost_scheme(4)
signals = list(signal_costs.keys())
#hill_solve.random_walker(map, signal_costs, signals)
sim_an_search.sim_an(map, signal_costs, signals, 200000, 1, 0.5)
analyse.print_costs(map, signal_costs)
