import readMap
import dfs
import draw
import sim_an_search
import analyse

#map = readMap.readStates('UnitedStates.txt')
map = readMap.read_complete_map('UnitedStatesdfs.txt')
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}

'''
dfs.dfs(map, signals)
with open("UnitedStatesdfs.txt", 'w') as text:
    for state in map:
        text.write(state.name)
        text.write(',')
        text.write(state.code)
        text.write(',')
        text.write(state.signal)
        text.write(',')
        for adjacent_state in state.adjacent_states:
            text.write(adjacent_state.code)
            text.write(',')
        text.write('\n')
'''
sim_an_search.hill_climber(map, signal_costs, signals, 200000, 5, 0.001)
freq = analyse.signal_frequentie(map)
old_costs = analyse.get_cost(freq, signal_costs)
for signal in freq:
    print(str(signal) + ' = ' + str(freq[signal]))
print(old_costs)
#draw.draw_america(map, signal_costs)