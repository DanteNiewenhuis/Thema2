import copy

def possible_signals(signals, state):
    print(signals)
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

def dfs(map, signals):
    state = find_next(map)
    if state == 0:
        return True
    possible_signal = possible_signals(signals, state)
    for signal in possible_signal:
        state.signal = signal
        checker = dfs(map, signals)
        if checker:
            return True
    return False
