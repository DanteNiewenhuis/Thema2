import copy
import analyse

def possible_signals(signals, state):
    result = copy.deepcopy(signals)
    for adjacent_state in state.adjacent_states:
        if adjacent_state.signal in result:
            result.remove(adjacent_state.signal)
    return result

def find_next(map):
    for state in map:
        if state.signal == 0:
            return state
    return 0

def reorder_possible_signals(possible_signal, amount_dic):
    result = []
    for signal in possible_signal:
        if signal in amount_dic:
            freq = amount_dic[signal]
        else:
            freq = 0
        checker = 0
        for x in range(len(result)):
            if possible_signal[x] in amount_dic:
                freq2 = amount_dic[possible_signal[x]]
            else:
                freq2 = 0
            if freq < freq2:
                result.insert(x, signal)
                checker = 1
                break
        if checker == 0:
            result.append(signal)
    return result

def dfs(map, signals):
    amount_dic = analyse.signal_frequentie(map)
    state = find_next(map)
    if state == 0:
        return True
    possible_signal = possible_signals(signals, state)
    possible_signal = reorder_possible_signals(possible_signal, amount_dic)
    for signal in possible_signal:
        state.signal = signal
        checker = dfs(map, signals)
        if checker:
            return True
    return False
