import readMap
import dfs
import analyse
import hill_solve
import sim_an_search


signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
cost1 = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
cost2 = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
cost3 = {'zA':16, 'zB':17, 'zC':31, 'zD':33, 'zE':36, 'zF':56, 'zG':57}
cost4 = {'zA':3, 'zB':34, 'zC':36, 'zD':39, 'zE':41, 'zF':43, 'zG':58}
costlist = [cost1, cost2, cost3, cost4]
lowest_costs = 1000
lowest_map = []
best_costs = 0
count = 1

for costs in costlist:
    for x in range(20):
        map = readMap.read_complete_map('UnitedStatesdfs.txt')
        map = sim_an_search.hill_climber(map, costs , signals, 200000, 5, 0.001)
        freq = analyse.signal_frequentie(map)
        old_costs = analyse.get_cost(freq, costs)
        if old_costs < lowest_costs:
            lowest_map = map
            best_costs = costs['zA']
            lowest_costs = old_costs
    print('cost:' + str(count))
    count += 1
print('Costscheme:' + str(best_costs))
print('Lowest costs:' + str(lowest_costs))

with open("bestmap.txt", 'w') as text:
    for state in lowest_map:
        text.write(state.name)
        text.write(',')
        text.write(state.code)
        text.write(',')
        text.write(state.signal)
        text.write('\n')