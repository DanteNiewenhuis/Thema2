import readMap
import draw
import analyse

map = readMap.read_complete_animation('testanimate.txt')

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}


freq = analyse.signal_frequentie(map[0])
costs = analyse.get_cost(freq, signal_costs)

for signal in freq:
    print(str(signal) + ' = ' + str(freq[signal]))

print(costs)
draw.draw_america(map[0], signal_costs)
