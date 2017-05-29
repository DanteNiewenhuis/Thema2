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
begintemp = {12:8, 19:4, 16:8, 3:14}
citer = 1
endtemp = [0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2]


with open("endtempstats.txt", 'a') as text:
    for c in costlist:
        for e in endtemp:
            m = 0
            print('end: ' + str(e))
            text.write(str(citer) + ',')
            text.write(str(begintemp[c['zA']]) + ',')
            text.write(str(e) + ',')
            for y in range(20):
                map = readMap.read_complete_map('Russiadfs.txt')
                map = sim_an_search.sim_an(map, c, signals, 200000, begintemp[c['zA']], e)
                freq = analyse.analyse_signal_frequentie(map)
                costs = analyse.get_cost(freq, c)
                text.write(str(costs) + ', ')
                m += costs
            print('mean: ' + str(m/20))
            text.write('\n')
        citer += 1

