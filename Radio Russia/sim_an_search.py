import random
import dfs
import analyse
import math
import matplotlib.pyplot as plt

def revert_changes(swapped_state):
    state = swapped_state[0]
    state.signal = swapped_state[1]

def swap_state(map, signals):
    swapped_state = random.choice(map)
    old_signal = swapped_state.signal
    possible_signals = dfs.possible_signals(signals, swapped_state)
    new_signal = random.choice(possible_signals)
    swapped_state.signal = new_signal
    return [swapped_state, old_signal]

def sigmodial_temperature(begin, end, n, x):
    a = (1/(n**2)) * math.log(begin/end)
    temperature = begin * math.exp(-a*(x**2))
    return temperature

def hill_climber(map, costs, signals):
    n = 10
    begin_temp = 1
    end_temp = 0.001
    #plot = []
    freq = analyse.signal_frequentie(map)
    old_costs = analyse.get_cost(freq, costs)
    for x in range(n):
        for y in range(100):
            checker = 0
            temperature = sigmodial_temperature(begin_temp, end_temp, n, x)
            if temperature <= 0:
                temperature = 1
            swapped_state = swap_state(map, signals)
            new_freq = analyse.signal_frequentie(map)
            new_costs = analyse.get_cost(new_freq, costs)
            improvement = old_costs - new_costs
            try:
                chance = math.exp(improvement/temperature)
                if chance > 1:
                    chance = 1
                #if chance > 1:
                    #print('temp = ' + str(temperature) + ' imp = '+ str(improvement) + ' chance = '+ str(chance))
                #plot.append(temperature)
            except OverflowError:
                chance = 0
            if random.random() < chance:
                checker = 1
            if checker == 1:
                old_costs = new_costs
            else:
                revert_changes(swapped_state)
    '''
    print(old_costs)
    plt.plot(plot)
    plt.ylabel('temp')
    plt.xlabel('iteraties')
    #plt.axis([0,1000,400,1000])
    plt.show()
    '''
    return map