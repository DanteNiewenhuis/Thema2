#run statistics and add to a cst file
import readMap
import dfs
import analyse
import hill_solve
import sim_an_search

loops = 100
dic = {}
best_costs = 1000
worst_costs = 0
#for l in range(loops):
map = readMap.readStates("UnitedStates.txt")
#print(analyse.analyse_adjacent_states(map))
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
algos = {sim_an_search.sigmoidal_temperature_3:[], sim_an_search.double_sigmoidal_temperature:[], sim_an_search.sinus_double_sigmoidal_temperature:[],
         sim_an_search.sinus_temperature:[], sim_an_search.linear_temperature:[]}

dfs.dfs(map, signals)
for heat, list in algos:
    for x in range(loops)
        sim_an_search.stats_climber(map, costs, signals, 200000, 5, 0.01, heat)
        freq = analyse.signal_frequentie(map)
        hill_costs = analyse.get_cost(freq, costs)
        list.append(hill_costs)
    for x in list



#with open("statsfile.txt", 'w') as text:
