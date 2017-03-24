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

def hill_climber(map, costs, signals):
    n = 500
    begin_temp = 200
    end_temp = 10
    #plot = []
    freq = analyse.signal_frequentie(map)
    old_costs = analyse.get_cost(freq, costs)
    for x in range(1,1000):
        checker = 0
        a = 1/(n**2) * math.log(begin_temp/end_temp)
        temperature = begin_temp * math.exp((-a)*(x**2))
        if temperature <= 0:
            temperature = 1
        #plot.append(temperature)
        swapped_state = swap_state(map, signals)
        new_freq = analyse.signal_frequentie(map)
        new_costs = analyse.get_cost(new_freq, costs)
        improvement = old_costs - new_costs
        try:
            chance = math.exp(improvement/temperature)
            if chance > 1:
                chance = 1
        except OverflowError:
            chance = 0
        if random.random() < chance:
            checker = 1
        if checker == 1:
            old_costs = new_costs
        else:
            revert_changes(swapped_state)
    '''
    plt.plot(plot)
    plt.ylabel('temp')
    plt.xlabel('iteraties')
    #plt.axis([0,1000,400,1000])
    plt.show()
    '''
    return map