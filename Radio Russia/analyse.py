import matplotlib.pyplot as plt
import numpy as np

def signal_frequentie(map):
    result = {}
    for state in map:
        if state.signal == 0:
            continue
        if state.signal in result:
            x = result.get(state.signal)
            x += 1
            result[state.signal] = x
        else:
            result[state.signal] = 1
    return result

def analyse_conflicts(map):
    for state in map:
        signal = state.signal
        for adjacent_state in state.adjacent_states:
            if signal == adjacent_state.signal:
                return 'conflict gevonden: ' + state.name + ' en ' + adjacent_state.name
    return 'geen conflicten'

def analyse_adjacent_states(map):
    for state in map:
        for adjacent_state in state.adjacent_states:
            if state not in adjacent_state.adjacent_states:
                return 'fout in kaart: geen ' + state.name + ' in ' + adjacent_state.name
    return 'geen fouten in kaart'

def get_cost(freqencies, costs):
    result = 0
    for signal in freqencies:
        cost = freqencies[signal] * costs[signal]
        result += cost
    return result

def get_frequencies_costs(list):
    dic = {}
    for cost in list:
        if cost in dic:
            x = dic[cost]
            x += 1
            dic[cost] = x
        else:
            dic[cost] = 1
    return dic


def bar_plot(dic):
    objects = sorted(dic.keys())
    performance = []
    for x in range(650, 850):
        if x in objects:
            performance.append(dic[x])
        else:
            performance.append(0)


    y_pos = np.arange(650, 850)
    width = 1

    ax = plt.subplot(111)
    ax.bar(y_pos + width, performance)

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.set_xticklabels([])
    ax.set_xticks(y_pos + width / 2)
    plt.show()