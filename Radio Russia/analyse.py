def analyse_signal_frequentie(map):
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

# based on https://www.pydanny.com/why-doesnt-python-have-switch-case.html
def get_cost_scheme(number):
    switcher = {
        1:{'zA': 12, 'zB': 26, 'zC': 27, 'zD': 30, 'zE': 37, 'zF': 39, 'zG': 41},
        2:{'zA': 19, 'zB': 20, 'zC': 21, 'zD': 23, 'zE': 36, 'zF': 37, 'zG': 38},
        3:{'zA': 16, 'zB': 17, 'zC': 31, 'zD': 33, 'zE': 36, 'zF': 56, 'zG': 57},
        4:{'zA': 3, 'zB': 34, 'zC': 36, 'zD': 39, 'zE': 41, 'zF': 43, 'zG': 58},
    }
    return switcher.get(number, 'please give a scheme between 1 and 4')

def print_costs(map, signal_costs, print_before='', print_after=''):
    freq = analyse_signal_frequentie(map)
    for signal in freq:
        print (str(signal) + ' = ' + str(freq[signal]))
    costs = get_cost(freq, signal_costs)
    print(str(print_before) + str(costs) + str(print_after))

def get_weight(scheme):
    sum = 0
    for cost in list(scheme.keys()):
        sum += scheme[cost]
    weights = []
    for cost in list(scheme.keys()):
        x = scheme[cost]
        y = x / sum
        weights.append(1 / y)
    sum_2 = 0
    for weight in weights:
        sum_2 += weight
    weights_2 = []
    for weight in weights:
        weights_2.append(weight / sum_2)
    signals = list(scheme.keys())
    weight_dict = {}
    for x in range(len(signals)):
        weight_dict[signals[x]] = weights_2[x]
    return weight_dict