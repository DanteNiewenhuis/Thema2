import readMap
import dfs
import analyse
import hill_solve
import sim_an_search

map = readMap.readStates("Oekraine.txt")
#print(analyse.analyse_adjacent_states(map))
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}

dfs.dfs(map, signals)

sim_an_search.hill_climber(map, costs, signals)
