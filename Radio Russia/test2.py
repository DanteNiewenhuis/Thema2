import readMap
import dfs
import hill_solve
import analyse


map = readMap.read_complete_map('Russiadfs5.csv')
signal_costs = analyse.get_cost_scheme(1)
analyse.print_costs(map, signal_costs)