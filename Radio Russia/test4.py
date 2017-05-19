import readMap
import dfs
import sim_an_search

map = readMap.readStates('UnitedStates.txt')

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}

dfs.dfs(map, signals)
sim_an_search.hill_climber(map, signal_costs, signals, 2000, 5, 0.001)

'''
with open('testanimate.txt','w') as text:
    for state in map:
        text.write(state.name)
        text.write(',')
        text.write(state.code)
        text.write(',')
        text.write(state.signal)
        text.write(',')
        for adj in state.adjacent_states:
            text.write(adj.name)
            text.write(',')
        text.write('next')
        text.write(',')
    text.write('\n')
'''