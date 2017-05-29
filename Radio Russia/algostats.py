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
#map = readMap.readStates("UnitedStates.txt")
#print(analyse.analyse_adjacent_states(map))
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
algos = {sim_an_search.sigmoidal_temperature:[],sim_an_search.sigmoidal_temperature_2:[],sim_an_search.sigmoidal_temperature_3:[],
         sim_an_search.double_sigmoidal_temperature:[], sim_an_search.sinus_double_sigmoidal_temperature:[],
         sim_an_search.sinus_temperature:[], sim_an_search.linear_temperature:[], sim_an_search.sinus_linear_temperature:[]}

with open("sinsigmoid.txt", 'w') as text:
    text.write('sinus_sigmoidal_temperature')
    text.write(',')
    for x in range(loops):
        map = readMap.read_complete_map("UnitedStatesdfs.txt")
        sim_an_search.stats_climber(map, costs, signals, 200000, 5, 0.01, sim_an_search.sinus_sigmoidal_temperature)
        freq = analyse.signal_frequentie(map)
        hill_costs = analyse.get_cost(freq, costs)
        text.write(str(hill_costs))
        text.write(',')
        print(str(x))
    text.write('\n')







