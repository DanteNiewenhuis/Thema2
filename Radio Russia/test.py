import readMap
import dfs
import analyse
import hill_solve
import sim_an_search

with open("analyse_sim.txt", 'w') as text:
    for n in [10,20,30]:
        for begin in [1,3,5,10,20]:
            for end in [0.01, 1, 2]:
                print (n, begin, end)
                loops = 100
                dic = {}
                best_costs = 1000
                worst_costs = 0
                for l in range(loops):
                    map = readMap.readStates("Oekraine.txt")
                    #print(analyse.analyse_adjacent_states(map))
                    signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
                    costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}

                    dfs.dfs(map, signals)

                    sim_an_search.hill_climber(map, costs, signals, n, begin, end)
                    freq = analyse.signal_frequentie(map)
                    hill_costs = analyse.get_cost(freq, costs)
                    if hill_costs < best_costs:
                        best_costs = hill_costs
                    if hill_costs > worst_costs:
                        worst_costs = hill_costs
                    if hill_costs in dic:
                        x = dic[hill_costs]
                        dic[hill_costs] = x + 1
                    else:
                        dic[hill_costs] = 1
                objects = sorted(dic.keys())
                average = 0
                for object in objects:
                    average += object * dic[object]
                average = round(average / loops)
                text.write(str(n) + "," + str(begin) + "," + str(end) +
                      "," + str(average) + "," + str(best_costs) + "," + str(worst_costs) + "\n")

'''
for state in best_map:
    print(str(state) + ' = ' + str(state.signal))
freq = analyse.signal_frequentie(best_map)
for signal in sorted(freq.keys()):
    print(str(signal) + ' = ' + str(freq[signal]))
costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
print(analyse.get_cost(freq, costs))
'''