import readMap
import dfs
import draw
import sim_an_search
import analyse

map = readMap.readStates('UnitedStates.txt')

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}

dfs.dfs(map, signals)
sim_an_search.hill_climber(map, costs, signals, 200, 5, 0.001)
freq = analyse.signal_frequentie(map)
hill_costs = analyse.get_cost(freq, costs)
draw.draw_america(map, hill_costs)