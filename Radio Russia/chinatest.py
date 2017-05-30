import analyse
import readMap
import sim_an_search

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
cost1 = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}
cost2 = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
cost3 = {'zA':16, 'zB':17, 'zC':31, 'zD':33, 'zE':36, 'zF':56, 'zG':57}
cost4 = {'zA':3, 'zB':34, 'zC':36, 'zD':39, 'zE':41, 'zF':43, 'zG':58}
costlist = [cost1, cost2, cost3, cost4]
begintemp = {1:9, 2:8, 3:9, 4:15}


with open('chinatemp.txt', 'a') as text:
    c = 1
    lowest_cost = 1500
    for y in range(50):
        map = readMap.read_complete_map('Chinadfs.txt')
        sim_an_search.sim_an(map, cost1, signals, begin_temp=begintemp[c], end_temp=0.5)
        freq = analyse.analyse_signal_frequentie(map)
        costs = analyse.get_cost(freq, cost1)
        if costs < lowest_cost:
            lowest_cost = costs
        print(c, y, lowest_cost)
    text.write(str(c) + ': ' + str(lowest_cost))
    text.write('\n')





