import readMap
import dfs
import analyse
import hill_solve
import sim_an_search
import time


signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
cost1 = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
cost2 = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
cost3 = {'zA':16, 'zB':17, 'zC':31, 'zD':33, 'zE':36, 'zF':56, 'zG':57}
cost4 = {'zA':3, 'zB':34, 'zC':36, 'zD':39, 'zE':41, 'zF':43, 'zG':58}
costlist = [cost1, cost2, cost3, cost4]
best_costs = 0
citer = 1
begintemp = [i for i in range(15,25)]
for i in [25,30,40,50,75,100,10000]:
    begintemp.append(i)
endtemp = [0.1, 1]

with open("tempstats.txt", 'w') as text:
    for c in costlist:
        lowest_map = []
        lowest_costs = 1200
        print('cost' + str(citer))
        for x in begintemp:
            print('beg: ' + str(x))
            print(time.clock())
            for e in endtemp:
                m = 0
                print('end: ' + str(e))
                text.write(str(citer) + ',')
                text.write(str(x) + ',')
                text.write(str(e) + ',')
                for y in range(10):
                    map = readMap.read_complete_map('UnitedStatesdfs.txt')
                    map = sim_an_search.sim_an(map, c, signals, 200000, x, e)
                    freq = analyse.analyse_signal_frequentie(map)
                    costs = analyse.get_cost(freq, c)
                    if citer == 4 and costs < lowest_costs:
                        lowest_map = map
                        lowest_costs = costs
                    text.write(str(costs) + ', ')
                    m += costs
                print('mean: ' + str(m/10))
                text.write('\n')
        if citer == 4:
            with open('newbestmap4.txt', 'w') as text2:
                for state in lowest_map:
                    text2.write(state.name)
                    text2.write(',')
                    text2.write(state.code)
                    text2.write(',')
                    text2.write(state.signal)
                    text2.write(',')
                    for adj in state.adjacent_states:
                        text2.write(adj.name)
                        text2.write(',')
                    text2.write('next')
                    text2.write(',')
                text2.write('\n')
            print('low4: ' + str(lowest_costs))
        citer += 1


