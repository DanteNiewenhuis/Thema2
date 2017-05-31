import analyse
import readMap
import sim_an_search

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
cost1 = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
cost2 = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
cost3 = {'zA':16, 'zB':17, 'zC':31, 'zD':33, 'zE':36, 'zF':56, 'zG':57}
cost4 = {'zA':3, 'zB':34, 'zC':36, 'zD':39, 'zE':41, 'zF':43, 'zG':58}
costlist = [cost1, cost2, cost3, cost4]
begintemp = [9, 5, 9, 15]
maplist = [readMap.read_complete_map('Ukrainedfs.txt'), readMap.read_complete_map('UnitedStatesdfs.txt'), readMap.read_complete_map('Russiadfs.txt')]


with open('temptation.txt', 'a') as text:
    for m in range(3):
        for c in range(4):
            lowest_cost = 2000
            for y in range(20):
                map = maplist[m]
                sim_an_search.sim_an(map, costlist[c], signals, begin_temp=begintemp[c], end_temp=0.5)
                freq = analyse.analyse_signal_frequentie(map)
                costs = analyse.get_cost(freq, costlist[c])
                if costs < lowest_cost:
                    lowest_cost = costs
                print(m, c + 1, y, lowest_cost)
            text.write(str(m) + str(c + 1) + ': ' + str(lowest_cost))
            text.write('\n')





