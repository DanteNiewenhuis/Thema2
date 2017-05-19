import analyse
import sim_an_search
import readMap
import hill_solve

map = readMap.read_complete_('UnitedStatesdfs.txt')

signal_costs = analyse.get_cost_scheme(4)
signals = list(signal_costs.keys())
hill_solve.random_walker(map, signal_costs, signals, iterations=1000)
#sim_an_search.sim_an(map, signal_costs, signals, 200000, 10, 0.1)
#analyse.print_costs(map, signal_costs)