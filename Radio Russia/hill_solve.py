import random
import dfs
import analyse
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
    plot = []
    numbers = []
    freq = analyse.signal_frequentie(map)
    old_costs = analyse.get_cost(freq, costs)
    counter = 0
    for x in range(200000):
        if counter == 400:
            break
        counter += 1
        plot.append(old_costs)
        numbers.append(x)
        swapped_state = swap_state(map, signals)
        new_freq = analyse.signal_frequentie(map)
        new_costs = analyse.get_cost(new_freq, costs)
        if new_costs <= old_costs:
            if new_costs < old_costs:
                counter = 0
            old_costs = new_costs
        else:
            revert_changes(swapped_state)
    '''
    plt.plot(plot)
    plt.ylabel('kosten')
    plt.xlabel('iteraties')
    plt.axis([-100,210000,900,1350])
    plt.show()
    '''
    return map
