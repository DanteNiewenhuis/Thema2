import readMap
import dfs
import analyse
import hill_solve
import sim_an_search

loops = 100
dic = {}
for x in range (loops):
    map = readMap.readStates("Oekraine.txt")
    #print(analyse.analyse_adjacent_states(map))
    signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
    costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}

    dfs.dfs(map, signals)

    sim_an_search.hill_climber(map, costs, signals)
    freq = analyse.signal_frequentie(map)
    best_costs = analyse.get_cost(freq, costs)
    if best_costs in dic:
        x = dic[best_costs]
        dic[best_costs] = x + 1
    else:
        dic[best_costs] = 1
objects = sorted(dic.keys())
average = 0
for object in objects:
    average += object * dic[object]
average = average / loops
print(average)
print(str(objects[0]) + ' = ' + str(dic[objects[0]]))
analyse.bar_plot(dic)


