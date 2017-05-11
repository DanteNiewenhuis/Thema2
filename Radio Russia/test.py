import readMap
import dfs
import hill_solve
import draw
import sim_an_search
import analyse
import copy

#map = readMap.readStates('UnitedStates.txt')

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
lowest_cost = 10000
lowest_map = 0
#dfs.dfs(map, signals)
for x in range(100):
    map = readMap.read_complete_map('best_map_america_2.txt')
    sim_an_search.hill_climber(map, signal_costs, signals, 200000, 5, 0.001)
    freq = analyse.signal_frequentie(map)
    costs = analyse.get_cost(freq, signal_costs)
    print(costs)
    if costs < lowest_cost:
        lowest_cost = costs
        lowest_map = copy.deepcopy(map)
freq = analyse.signal_frequentie(lowest_map)
costs = analyse.get_cost(freq, signal_costs)
print('lowest = ' + str(costs))
with open('best_map_america_2_new.txt','w') as text:
    for state in lowest_map:
        text.write(state.name)
        text.write(',')
        text.write(state.code)
        text.write(',')
        text.write(state.signal)
        text.write(',')
        for adj_state in state.adjacent_states:
            text.write(adj_state.code)
            text.write(',')
        text.write('\n')

#draw.draw_america(map, signal_costs)