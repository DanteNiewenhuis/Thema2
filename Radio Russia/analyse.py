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
        5: {'zA': 1, 'zB': 37, 'zC': 38, 'zD': 39, 'zE': 41, 'zF': 43, 'zG': 58},
        6: {'zA': 1, 'zB': 11, 'zC': 12, 'zD': 13, 'zE': 14, 'zF': 15, 'zG': 16},
        7: {'zA': 1, 'zB': 21, 'zC': 22, 'zD': 23, 'zE': 24, 'zF': 25, 'zG': 26},
        8: {'zA': 1, 'zB': 31, 'zC': 32, 'zD': 33, 'zE': 34, 'zF': 35, 'zG': 36},
        9: {'zA': 1, 'zB': 41, 'zC': 42, 'zD': 43, 'zE': 44, 'zF': 45, 'zG': 46},
        10: {'zA': 1, 'zB': 51, 'zC': 52, 'zD': 53, 'zE': 54, 'zF': 55, 'zG': 56},
        11: {'zA': 1, 'zB': 61, 'zC': 62, 'zD': 63, 'zE': 64, 'zF': 65, 'zG': 66},
        12: {'zA': 3001, 'zB': 3002, 'zC': 3003, 'zD': 3004, 'zE': 3005, 'zF': 3006, 'zG': 3007},
        13: {'zA': 3001, 'zB': 3052, 'zC': 3053, 'zD': 3054, 'zE': 3055, 'zF': 3056, 'zG': 3057},
        14: {'zA': 1, 'zB': 2, 'zC': 13, 'zD': 14, 'zE': 15, 'zF': 16, 'zG': 17},
        15: {'zA': 1, 'zB': 2, 'zC': 23, 'zD': 24, 'zE': 25, 'zF': 26, 'zG': 27},
        16: {'zA': 1, 'zB': 2, 'zC': 33, 'zD': 34, 'zE': 35, 'zF': 36, 'zG': 37},
        17: {'zA': 1, 'zB': 2, 'zC': 43, 'zD': 44, 'zE': 45, 'zF': 46, 'zG': 47},
        18: {'zA': 1, 'zB': 2, 'zC': 3, 'zD': 43, 'zE': 44, 'zF': 45, 'zG': 46},
        19: {'zA': 10, 'zB': 11, 'zC': 12, 'zD': 13, 'zE': 14, 'zF': 15, 'zG': 56},
        20: {'zA': 10, 'zB': 11, 'zC': 12, 'zD': 13, 'zE': 14, 'zF': 35, 'zG': 56},
        21: {'zA': 11, 'zB': 12, 'zC': 13, 'zD': 14, 'zE': 15, 'zF': 16, 'zG': 17},
    }
    return switcher.get(number, 'please give a scheme between 1 and 4')

def print_costs(map, signal_costs, print_before='', print_after=''):
    freq = analyse_signal_frequentie(map)
    for signal in list(signal_costs.keys()):
        if signal in freq:
            print(str(signal) + ' = ' + str(freq[signal]))
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